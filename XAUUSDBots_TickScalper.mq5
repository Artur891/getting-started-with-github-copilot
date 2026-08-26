//+------------------------------------------------------------------+
//|                                     XAUUSDBots_TickScalper.mq5   |
//|                                      Copyright 2024, AI Engineer |
//+------------------------------------------------------------------+
#property copyright "AI Engineer"
#property link      ""
#property version   "1.00"

#include <Trade\Trade.mqh>
#include <Trade\PositionInfo.mqh>
#include <Trade\SymbolInfo.mqh>
#include <Trade\OrderInfo.mqh>
#include <Controls\Dialog.mqh>
#include <Controls\Button.mqh>
#include <Controls\Label.mqh>

//--- Input parameters
input group "Money Management"
input double   InpLotSize        = 0.01;      // Fixed Lot Size (if Risk % is 0)
input double   InpRiskPercent    = 1.0;       // Risk in % (0 to use Fixed Lot)
input double   InpMinMarginLevel = 150.0;     // Minimum Margin Level %

input group "Trading Parameters"
input int      InpStopLoss       = 50;        // Stop Loss (in points)
input int      InpTakeProfit     = 100;       // Take Profit (in points)
input int      InpPendingDistance= 20;        // Distance for Pending Orders (points)
input int      InpOrderExpiration= 60;        // Pending Order Expiration (seconds)

input group "Trailing Stop"
input int      InpTrailingStart  = 30;        // Trailing Start (in points)
input int      InpTrailingStep   = 10;        // Trailing Step (in points)

input group "Volatility & Strategy"
input double   InpVolMultiplier  = 3.0;       // Volatility Limit Multiplier (Spread * X)
input int      InpMaxSpread      = 40;        // Maximum Spread allowed (points)

enum ENUM_FILTER_TYPE {
    FILTER_NONE = 0,    // No Filter (Trade both ways)
    FILTER_MA = 1,      // Moving Average
    FILTER_BB = 2,      // Bollinger Bands
    FILTER_ENVELOPES=3  // Envelopes
};
input ENUM_FILTER_TYPE InpFilterType = FILTER_NONE; // Selected Filter

//--- Global variables
CTrade         m_trade;
CSymbolInfo    m_symbol;
CPositionInfo  m_position;
COrderInfo     m_order;

bool isTradingEnabled = true;

//--- Indicator handles
int handleMA = INVALID_HANDLE;
int handleBB = INVALID_HANDLE;
int handleEnv = INVALID_HANDLE;

//--- GUI elements
CAppDialog     AppWindow;
CButton        BtnToggleTrading;
CButton        BtnCloseAll;
CLabel         LblSpread;
CLabel         LblVolatility;
CLabel         LblStatus;

//+------------------------------------------------------------------+
//| Helper to create GUI                                             |
//+------------------------------------------------------------------+
bool CreateGUI()
{
   if(!AppWindow.Create(0, "XAUUSD Scalper", 0, 20, 20, 280, 200))
      return false;

   if(!BtnToggleTrading.Create(0, "BtnToggle", 0, 10, 30, 120, 60))
      return false;
   BtnToggleTrading.Text("STOP TRADING");
   BtnToggleTrading.ColorBackground(clrGreen);
   AppWindow.Add(BtnToggleTrading);

   if(!BtnCloseAll.Create(0, "BtnClose", 0, 130, 30, 240, 60))
      return false;
   BtnCloseAll.Text("CLOSE ALL");
   BtnCloseAll.ColorBackground(clrRed);
   AppWindow.Add(BtnCloseAll);

   if(!LblSpread.Create(0, "LblSpread", 0, 10, 80, 200, 100))
      return false;
   LblSpread.Text("Spread: 0");
   AppWindow.Add(LblSpread);

   if(!LblVolatility.Create(0, "LblVol", 0, 10, 110, 200, 130))
      return false;
   LblVolatility.Text("Volatility: 0 / 0");
   AppWindow.Add(LblVolatility);

   if(!LblStatus.Create(0, "LblStat", 0, 10, 140, 200, 160))
      return false;
   LblStatus.Text("Status: OK");
   AppWindow.Add(LblStatus);

   AppWindow.Run();
   return true;
}

//+------------------------------------------------------------------+
//| Expert initialization function                                   |
//+------------------------------------------------------------------+
int OnInit()
  {
//---
   if(!m_symbol.Name(_Symbol))
      return(INIT_FAILED);
   m_symbol.Refresh();

   m_trade.SetExpertMagicNumber(1337);

   if(!CreateGUI())
   {
      Print("Failed to create GUI");
      return(INIT_FAILED);
   }

   // Initialize indicators based on selected filter type
   if(InpFilterType == FILTER_MA)
     {
      handleMA = iMA(_Symbol, PERIOD_M1, 50, 0, MODE_EMA, PRICE_CLOSE);
      if(handleMA == INVALID_HANDLE)
        {
         Print("Failed to create MA indicator handle");
         return(INIT_FAILED);
        }
     }
   else if(InpFilterType == FILTER_BB)
     {
      handleBB = iBands(_Symbol, PERIOD_M1, 20, 0, 2.0, PRICE_CLOSE);
      if(handleBB == INVALID_HANDLE)
        {
         Print("Failed to create Bollinger Bands handle");
         return(INIT_FAILED);
        }
     }
   else if(InpFilterType == FILTER_ENVELOPES)
     {
      handleEnv = iEnvelopes(_Symbol, PERIOD_M1, 14, 0, MODE_SMA, PRICE_CLOSE, 0.1);
      if(handleEnv == INVALID_HANDLE)
        {
         Print("Failed to create Envelopes handle");
         return(INIT_FAILED);
        }
     }

//---
   return(INIT_SUCCEEDED);
  }

//+------------------------------------------------------------------+
//| Expert deinitialization function                                 |
//+------------------------------------------------------------------+
void OnDeinit(const int reason)
  {
//---
   AppWindow.Destroy(reason);

   if(handleMA != INVALID_HANDLE) IndicatorRelease(handleMA);
   if(handleBB != INVALID_HANDLE) IndicatorRelease(handleBB);
   if(handleEnv != INVALID_HANDLE) IndicatorRelease(handleEnv);
  }

//+------------------------------------------------------------------+
//| ChartEvent function                                              |
//+------------------------------------------------------------------+
void OnChartEvent(const int id,
                  const long &lparam,
                  const double &dparam,
                  const string &sparam)
  {
   AppWindow.ChartEvent(id, lparam, dparam, sparam);

   if(id == CHARTEVENT_CUSTOM+ON_CLICK)
     {
      if(sparam == "BtnToggle")
        {
         isTradingEnabled = !isTradingEnabled;
         if(isTradingEnabled)
           {
            BtnToggleTrading.Text("STOP TRADING");
            BtnToggleTrading.ColorBackground(clrGreen);
           }
         else
           {
            BtnToggleTrading.Text("START TRADING");
            BtnToggleTrading.ColorBackground(clrRed);
           }
        }
      else if(sparam == "BtnClose")
        {
         CloseAllPositionsAndOrders();
        }
     }
  }

//+------------------------------------------------------------------+
//| Helper to calculate lot size                                     |
//+------------------------------------------------------------------+
double CalculateLotSize(double stopLossPoints)
{
   if(InpRiskPercent <= 0)
      return InpLotSize;

   double riskMoney = AccountInfoDouble(ACCOUNT_BALANCE) * (InpRiskPercent / 100.0);
   double tickValue = SymbolInfoDouble(_Symbol, SYMBOL_TRADE_TICK_VALUE);
   double tickSize = SymbolInfoDouble(_Symbol, SYMBOL_TRADE_TICK_SIZE);

   if(tickValue == 0 || tickSize == 0) return InpLotSize;

   double lossPerLot = (stopLossPoints * _Point / tickSize) * tickValue;
   if(lossPerLot == 0) return InpLotSize;

   double lot = riskMoney / lossPerLot;

   double minLot = SymbolInfoDouble(_Symbol, SYMBOL_VOLUME_MIN);
   double maxLot = SymbolInfoDouble(_Symbol, SYMBOL_VOLUME_MAX);
   double step = SymbolInfoDouble(_Symbol, SYMBOL_VOLUME_STEP);

   lot = MathMax(lot, minLot);
   lot = MathMin(lot, maxLot);
   lot = MathRound(lot / step) * step;

   return lot;
}

//+------------------------------------------------------------------+
//| Check Filter Direction                                           |
//+------------------------------------------------------------------+
int CheckFilterDirection(double currentPrice)
{
   if(InpFilterType == FILTER_NONE) return 0; // 0 means both ways allowed

   if(InpFilterType == FILTER_MA && handleMA != INVALID_HANDLE)
   {
      double ma[1];
      if(CopyBuffer(handleMA, 0, 0, 1, ma) > 0)
      {
         if(currentPrice > ma[0]) return 1; // 1 means only BUY allowed
         if(currentPrice < ma[0]) return -1; // -1 means only SELL allowed
      }
   }
   else if(InpFilterType == FILTER_BB && handleBB != INVALID_HANDLE)
   {
      double upper[1], lower[1];
      if(CopyBuffer(handleBB, 1, 0, 1, upper) > 0 && CopyBuffer(handleBB, 2, 0, 1, lower) > 0)
      {
         if(currentPrice > upper[0]) return 1;
         if(currentPrice < lower[0]) return -1;
      }
   }
   else if(InpFilterType == FILTER_ENVELOPES && handleEnv != INVALID_HANDLE)
   {
      double upper[1], lower[1];
      if(CopyBuffer(handleEnv, 0, 0, 1, upper) > 0 && CopyBuffer(handleEnv, 1, 0, 1, lower) > 0)
      {
         if(currentPrice > upper[0]) return 1;
         if(currentPrice < lower[0]) return -1;
      }
   }

   return 0; // Default: allow both if buffers fail
}

//+------------------------------------------------------------------+
//| Manage Trailing Stop                                             |
//+------------------------------------------------------------------+
void ManageTrailingStop()
{
   if(InpTrailingStart <= 0 || InpTrailingStep <= 0) return;

   for(int i = PositionsTotal() - 1; i >= 0; i--)
   {
      if(m_position.SelectByIndex(i) && m_position.Symbol() == _Symbol && m_position.Magic() == 1337)
      {
         double currentPrice = (m_position.PositionType() == POSITION_TYPE_BUY) ? m_symbol.Bid() : m_symbol.Ask();
         double openPrice = m_position.PriceOpen();
         double currentSL = m_position.StopLoss();
         double currentTP = m_position.TakeProfit();

         if(m_position.PositionType() == POSITION_TYPE_BUY)
         {
            double profitPoints = (currentPrice - openPrice) / _Point;
            if(profitPoints >= InpTrailingStart)
            {
               double newSL = currentPrice - (InpTrailingStart * _Point);
               if(currentSL < newSL - (InpTrailingStep * _Point) || currentSL == 0)
               {
                  m_trade.PositionModify(m_position.Ticket(), newSL, currentTP);
               }
            }
         }
         else if(m_position.PositionType() == POSITION_TYPE_SELL)
         {
            double profitPoints = (openPrice - currentPrice) / _Point;
            if(profitPoints >= InpTrailingStart)
            {
               double newSL = currentPrice + (InpTrailingStart * _Point);
               if(currentSL > newSL + (InpTrailingStep * _Point) || currentSL == 0)
               {
                  m_trade.PositionModify(m_position.Ticket(), newSL, currentTP);
               }
            }
         }
      }
   }
}

//+------------------------------------------------------------------+
//| Close all logic                                                  |
//+------------------------------------------------------------------+
void CloseAllPositionsAndOrders()
{
   for(int i = PositionsTotal() - 1; i >= 0; i--)
   {
      if(m_position.SelectByIndex(i) && m_position.Symbol() == _Symbol && m_position.Magic() == 1337)
      {
         m_trade.PositionClose(m_position.Ticket());
      }
   }
   for(int i = OrdersTotal() - 1; i >= 0; i--)
   {
      if(m_order.SelectByIndex(i) && m_order.Symbol() == _Symbol && m_order.Magic() == 1337)
      {
         m_trade.OrderDelete(m_order.Ticket());
      }
   }
   LblStatus.Text("Status: All Closed.");
}

//+------------------------------------------------------------------+
//| Expert tick function                                             |
//+------------------------------------------------------------------+
void OnTick()
  {
   if(!isTradingEnabled) return;

   m_symbol.RefreshRates();

   // Update Spread GUI
   int spread = (int)SymbolInfoInteger(_Symbol, SYMBOL_SPREAD);
   LblSpread.Text("Spread: " + IntegerToString(spread));

   // Margin Check
   if(AccountInfoDouble(ACCOUNT_MARGIN_LEVEL) < InpMinMarginLevel && AccountInfoDouble(ACCOUNT_MARGIN) > 0)
   {
      LblStatus.Text("Status: Low Margin!");
      return;
   }

   // Spread Check
   if(spread > InpMaxSpread)
   {
      LblStatus.Text("Status: High Spread!");
      return;
   }

   LblStatus.Text("Status: Scanning...");

   // Calculate Volatility
   double m1High[1], m1Low[1];
   if(CopyHigh(_Symbol, PERIOD_M1, 0, 1, m1High) <= 0 || CopyLow(_Symbol, PERIOD_M1, 0, 1, m1Low) <= 0) return;

   double candleRange = (m1High[0] - m1Low[0]) / _Point;
   double volatilityLimit = spread * InpVolMultiplier;

   LblVolatility.Text(StringFormat("Vol: %.1f / %.1f", candleRange, volatilityLimit));

   // Trailing Stop Management
   ManageTrailingStop();

   // Check if we already have open orders or positions
   int myOrders = 0;
   for(int i = 0; i < OrdersTotal(); i++)
   {
      if(m_order.SelectByIndex(i) && m_order.Symbol() == _Symbol && m_order.Magic() == 1337) myOrders++;
   }
   int myPositions = 0;
   for(int i = 0; i < PositionsTotal(); i++)
   {
      if(m_position.SelectByIndex(i) && m_position.Symbol() == _Symbol && m_position.Magic() == 1337) myPositions++;
   }

   // Only place new orders if none exist
   if(myOrders == 0 && myPositions == 0)
   {
      if(candleRange > volatilityLimit)
      {
         double currentPrice = m_symbol.Ask();
         int filterDirection = CheckFilterDirection(currentPrice);

         double lot = CalculateLotSize(InpStopLoss);
         datetime expiration = TimeCurrent() + InpOrderExpiration;

         if(filterDirection >= 0) // Buy allowed
         {
            double buyPrice = m_symbol.Ask() + (InpPendingDistance * _Point);
            double sl = buyPrice - (InpStopLoss * _Point);
            double tp = buyPrice + (InpTakeProfit * _Point);
            m_trade.BuyStop(lot, buyPrice, _Symbol, sl, tp, ORDER_TIME_SPECIFIED, expiration);
         }

         if(filterDirection <= 0) // Sell allowed
         {
            double sellPrice = m_symbol.Bid() - (InpPendingDistance * _Point);
            double sl = sellPrice + (InpStopLoss * _Point);
            double tp = sellPrice - (InpTakeProfit * _Point);
            m_trade.SellStop(lot, sellPrice, _Symbol, sl, tp, ORDER_TIME_SPECIFIED, expiration);
         }
      }
   }
  }
//+------------------------------------------------------------------+
