import json

# Pairing groups based on pair characteristics
PAIRS_LIQUID_MAJORS = ["EURUSD", "GBPUSD", "AUDUSD", "USDCAD"]
PAIRS_VOLATILE_EXOTIC_CROSSES = ["GOLD", "GBPJPY", "GBPAUD", "EURNZD", "USDZAR"]
PAIRS_RANGING_MEAN_REVERSION = ["EURGBP", "USDJPY", "USDCAD"]
PAIRS_ALL_TRENDING = ["GOLD", "EURUSD", "GBPUSD", "GBPJPY", "AUDUSD"]

base_strategies = [
    {
        "id": "SMC_Liquidity_Sweep",
        "desc_buy": "LuxAlgo Smart Money Concepts Buy. Entry on liquidity sweep below old lows with bullish confirmation. Winrate > 70%.",
        "desc_sell": "LuxAlgo Smart Money Concepts Sell. Entry on liquidity sweep above old highs with bearish confirmation. Winrate > 70%.",
        "primary_tf": "M15",
        "conf_tfs": ["H1", "M5"],
        "recommended_pairs": PAIRS_LIQUID_MAJORS + ["GOLD"],
        "atr_buffer": 1.2, # Standard + extra for Gold
        "conditions_buy": [
            {"type": "liquidity_sweep", "timeframe": "M15", "side": "low", "lookback": 50},
            {"type": "candle_pattern", "timeframe": "M5", "patterns": ["bullish_pinbar", "bullish_engulfing"], "mode": "any"}
        ],
        "conditions_sell": [
            {"type": "liquidity_sweep", "timeframe": "M15", "side": "high", "lookback": 50},
            {"type": "candle_pattern", "timeframe": "M5", "patterns": ["bearish_pinbar", "bearish_engulfing"], "mode": "any"}
        ]
    },
    {
        "id": "FVG_Trend_Continuation",
        "desc_buy": "LuxAlgo Fair Value Gap Buy. Tap into a bullish FVG in an uptrend for continuation.",
        "desc_sell": "LuxAlgo Fair Value Gap Sell. Tap into a bearish FVG in a downtrend for continuation.",
        "primary_tf": "M15",
        "conf_tfs": ["H1"],
        "recommended_pairs": PAIRS_ALL_TRENDING,
        "atr_buffer": 1.5, # Needs room to rebalance the gap
        "conditions_buy": [
            {"type": "market_structure", "timeframe": "H1", "direction": "up", "lookback": 50},
            {"type": "fvg_tap", "timeframe": "M15", "direction": "bullish"}
        ],
        "conditions_sell": [
            {"type": "market_structure", "timeframe": "H1", "direction": "down", "lookback": 50},
            {"type": "fvg_tap", "timeframe": "M15", "direction": "bearish"}
        ]
    },
    {
        "id": "Machine_Learning_KNN",
        "desc_buy": "LuxAlgo ML KNN Classification Buy. Predictive model signals bullish regime.",
        "desc_sell": "LuxAlgo ML KNN Classification Sell. Predictive model signals bearish regime.",
        "primary_tf": "H1",
        "conf_tfs": ["H4"],
        "recommended_pairs": ["EURUSD", "GBPUSD", "AUDUSD"],
        "atr_buffer": 1.0, # Clean math models usually work better on clean majors
        "conditions_buy": [
            {"type": "ml_knn_signal", "timeframe": "H1", "direction": "bullish", "confidence_min": 80}
        ],
        "conditions_sell": [
            {"type": "ml_knn_signal", "timeframe": "H1", "direction": "bearish", "confidence_min": 80}
        ]
    },
    {
        "id": "Order_Block_Reversal",
        "desc_buy": "LuxAlgo Order Block Reversal Buy. Price touches bullish order block with RSI divergence.",
        "desc_sell": "LuxAlgo Order Block Reversal Sell. Price touches bearish order block with RSI divergence.",
        "primary_tf": "M15",
        "conf_tfs": ["H1"],
        "recommended_pairs": PAIRS_LIQUID_MAJORS + ["USDJPY"],
        "atr_buffer": 1.2,
        "conditions_buy": [
            {"type": "order_block_tap", "timeframe": "M15", "direction": "bullish"},
            {"type": "rsi_divergence", "timeframe": "M15", "direction": "bullish"}
        ],
        "conditions_sell": [
            {"type": "order_block_tap", "timeframe": "M15", "direction": "bearish"},
            {"type": "rsi_divergence", "timeframe": "M15", "direction": "bearish"}
        ]
    },
    {
        "id": "SuperTrend_Pullback",
        "desc_buy": "LuxAlgo Supertrend Pullback Buy. Entering long on retracement to bullish Supertrend.",
        "desc_sell": "LuxAlgo Supertrend Pullback Sell. Entering short on retracement to bearish Supertrend.",
        "primary_tf": "H1",
        "conf_tfs": ["D1"],
        "recommended_pairs": PAIRS_ALL_TRENDING + ["GBPJPY"],
        "atr_buffer": 1.5, # Trends need breathing room
        "conditions_buy": [
            {"type": "supertrend", "timeframe": "D1", "direction": "bullish"},
            {"type": "pullback_to_band", "timeframe": "H1", "band": "supertrend"}
        ],
        "conditions_sell": [
            {"type": "supertrend", "timeframe": "D1", "direction": "bearish"},
            {"type": "pullback_to_band", "timeframe": "H1", "band": "supertrend"}
        ]
    },
    {
        "id": "Volume_Profile_POC_Bounce",
        "desc_buy": "LuxAlgo Volume Profile Buy. Bounce off the Point of Control (POC) in a rising value area.",
        "desc_sell": "LuxAlgo Volume Profile Sell. Rejection from the Point of Control (POC) in a falling value area.",
        "primary_tf": "M30",
        "conf_tfs": ["H4"],
        "recommended_pairs": ["GOLD", "EURUSD", "GBPUSD", "USDCAD"],
        "atr_buffer": 1.1,
        "conditions_buy": [
            {"type": "poc_bounce", "timeframe": "M30", "direction": "bullish"}
        ],
        "conditions_sell": [
            {"type": "poc_bounce", "timeframe": "M30", "direction": "bearish"}
        ]
    },
    {
        "id": "Trend_Tracer_Breakout",
        "desc_buy": "LuxAlgo Trend Tracer Buy. High momentum breakout confirmed by ADX.",
        "desc_sell": "LuxAlgo Trend Tracer Sell. High momentum breakdown confirmed by ADX.",
        "primary_tf": "M15",
        "conf_tfs": ["H1"],
        "recommended_pairs": PAIRS_VOLATILE_EXOTIC_CROSSES, # High momentum pairs
        "atr_buffer": 1.8, # Volatile pairs breakout needs huge stop buffers
        "conditions_buy": [
            {"type": "adx", "timeframe": "H1", "min": 25},
            {"type": "trend_tracer_break", "timeframe": "M15", "direction": "bullish"}
        ],
        "conditions_sell": [
            {"type": "adx", "timeframe": "H1", "min": 25},
            {"type": "trend_tracer_break", "timeframe": "M15", "direction": "bearish"}
        ]
    },
    {
        "id": "Oscillator_Matrix_Confluence",
        "desc_buy": "LuxAlgo Oscillator Matrix Buy. Multiple timeframes oscillators align bullish.",
        "desc_sell": "LuxAlgo Oscillator Matrix Sell. Multiple timeframes oscillators align bearish.",
        "primary_tf": "M15",
        "conf_tfs": ["M5", "M30", "H1"],
        "recommended_pairs": PAIRS_RANGING_MEAN_REVERSION,
        "atr_buffer": 0.8, # Tighter stops for ranging markets
        "conditions_buy": [
            {"type": "oscillator_confluence", "timeframes": ["M5", "M15", "M30", "H1"], "direction": "bullish"}
        ],
        "conditions_sell": [
            {"type": "oscillator_confluence", "timeframes": ["M5", "M15", "M30", "H1"], "direction": "bearish"}
        ]
    },
    {
        "id": "Dynamic_SNR_Break",
        "desc_buy": "LuxAlgo Dynamic Support/Resistance Buy. Breakout and retest of dynamic resistance.",
        "desc_sell": "LuxAlgo Dynamic Support/Resistance Sell. Breakdown and retest of dynamic support.",
        "primary_tf": "H1",
        "conf_tfs": ["H4"],
        "recommended_pairs": ["GOLD", "GBPJPY", "EURUSD", "AUDUSD"],
        "atr_buffer": 1.3,
        "conditions_buy": [
            {"type": "snr_break_retest", "timeframe": "H1", "level_type": "resistance"}
        ],
        "conditions_sell": [
            {"type": "snr_break_retest", "timeframe": "H1", "level_type": "support"}
        ]
    },
    {
        "id": "EMA_Cloud_Trend",
        "desc_buy": "LuxAlgo EMA Cloud Buy. Price above cloud with MACD bullish cross.",
        "desc_sell": "LuxAlgo EMA Cloud Sell. Price below cloud with MACD bearish cross.",
        "primary_tf": "M15",
        "conf_tfs": ["H1"],
        "recommended_pairs": PAIRS_ALL_TRENDING,
        "atr_buffer": 1.2,
        "conditions_buy": [
            {"type": "ema_cloud", "timeframe": "H1", "relation": "above"},
            {"type": "macd_cross", "timeframe": "M15", "direction": "bullish"}
        ],
        "conditions_sell": [
            {"type": "ema_cloud", "timeframe": "H1", "relation": "below"},
            {"type": "macd_cross", "timeframe": "M15", "direction": "bearish"}
        ]
    },
    {
        "id": "VWAP_Mean_Reversion",
        "desc_buy": "LuxAlgo VWAP Buy. Price overextended to the downside returning to VWAP.",
        "desc_sell": "LuxAlgo VWAP Sell. Price overextended to the upside returning to VWAP.",
        "primary_tf": "M5",
        "conf_tfs": ["M15"],
        "recommended_pairs": PAIRS_RANGING_MEAN_REVERSION + ["USDCAD"],
        "atr_buffer": 0.9,
        "conditions_buy": [
            {"type": "vwap_deviation", "timeframe": "M5", "std_dev": -2},
            {"type": "reversal_pattern", "timeframe": "M5", "direction": "bullish"}
        ],
        "conditions_sell": [
            {"type": "vwap_deviation", "timeframe": "M5", "std_dev": 2},
            {"type": "reversal_pattern", "timeframe": "M5", "direction": "bearish"}
        ]
    },
    {
        "id": "Supply_Demand_Zones",
        "desc_buy": "LuxAlgo Supply & Demand Buy. Price rejects from Demand zone with Stochastic oversold.",
        "desc_sell": "LuxAlgo Supply & Demand Sell. Price rejects from Supply zone with Stochastic overbought.",
        "primary_tf": "M30",
        "conf_tfs": ["H4"],
        "recommended_pairs": ["GOLD", "EURUSD", "GBPUSD", "USDJPY", "GBPJPY"],
        "atr_buffer": 1.4,
        "conditions_buy": [
            {"type": "zone_rejection", "timeframe": "M30", "zone_type": "demand"},
            {"type": "stochastic", "timeframe": "M30", "state": "oversold"}
        ],
        "conditions_sell": [
            {"type": "zone_rejection", "timeframe": "M30", "zone_type": "supply"},
            {"type": "stochastic", "timeframe": "M30", "state": "overbought"}
        ]
    },
    {
        "id": "Bollinger_Band_Squeeze",
        "desc_buy": "LuxAlgo BB Squeeze Buy. Volatility expansion to the upside.",
        "desc_sell": "LuxAlgo BB Squeeze Sell. Volatility expansion to the downside.",
        "primary_tf": "H1",
        "conf_tfs": ["H4"],
        "recommended_pairs": PAIRS_VOLATILE_EXOTIC_CROSSES + ["EURUSD"],
        "atr_buffer": 1.6,
        "conditions_buy": [
            {"type": "bb_squeeze_break", "timeframe": "H1", "direction": "bullish"}
        ],
        "conditions_sell": [
            {"type": "bb_squeeze_break", "timeframe": "H1", "direction": "bearish"}
        ]
    },
    {
        "id": "Ichimoku_Cloud_Breakout",
        "desc_buy": "LuxAlgo Ichimoku Buy. Kumo cloud breakout with Tenkan/Kijun cross.",
        "desc_sell": "LuxAlgo Ichimoku Sell. Kumo cloud breakdown with Tenkan/Kijun cross.",
        "primary_tf": "H4",
        "conf_tfs": ["D1"],
        "recommended_pairs": ["USDJPY", "GBPJPY", "EURUSD", "GOLD"],
        "atr_buffer": 1.5,
        "conditions_buy": [
            {"type": "kumo_breakout", "timeframe": "H4", "direction": "bullish"},
            {"type": "tenkan_kijun_cross", "timeframe": "H4", "direction": "bullish"}
        ],
        "conditions_sell": [
            {"type": "kumo_breakout", "timeframe": "H4", "direction": "bearish"},
            {"type": "tenkan_kijun_cross", "timeframe": "H4", "direction": "bearish"}
        ]
    },
    {
        "id": "Divergence_Catcher",
        "desc_buy": "LuxAlgo Divergence Catcher Buy. Regular bullish divergence on RSI.",
        "desc_sell": "LuxAlgo Divergence Catcher Sell. Regular bearish divergence on RSI.",
        "primary_tf": "M15",
        "conf_tfs": ["H1"],
        "recommended_pairs": PAIRS_RANGING_MEAN_REVERSION + ["AUDUSD"],
        "atr_buffer": 0.9,
        "conditions_buy": [
            {"type": "divergence", "timeframe": "M15", "indicator": "RSI", "direction": "regular_bullish"}
        ],
        "conditions_sell": [
            {"type": "divergence", "timeframe": "M15", "indicator": "RSI", "direction": "regular_bearish"}
        ]
    },
    {
        "id": "Heikin_Ashi_Smoothed",
        "desc_buy": "LuxAlgo Smoothed HA Buy. Trend continuation on smoothed Heikin Ashi.",
        "desc_sell": "LuxAlgo Smoothed HA Sell. Trend continuation on smoothed Heikin Ashi.",
        "primary_tf": "H1",
        "conf_tfs": ["H4"],
        "recommended_pairs": ["GBPUSD", "GBPJPY", "GOLD", "USDCAD"],
        "atr_buffer": 1.4,
        "conditions_buy": [
            {"type": "heikin_ashi_smoothed", "timeframe": "H4", "color": "green"},
            {"type": "pullback_completion", "timeframe": "H1", "direction": "bullish"}
        ],
        "conditions_sell": [
            {"type": "heikin_ashi_smoothed", "timeframe": "H4", "color": "red"},
            {"type": "pullback_completion", "timeframe": "H1", "direction": "bearish"}
        ]
    },
    {
        "id": "Pivot_Point_Reversal",
        "desc_buy": "LuxAlgo Pivot Point Buy. Reversal from S1 or S2 pivot level.",
        "desc_sell": "LuxAlgo Pivot Point Sell. Reversal from R1 or R2 pivot level.",
        "primary_tf": "M15",
        "conf_tfs": ["H1"],
        "recommended_pairs": PAIRS_LIQUID_MAJORS + PAIRS_RANGING_MEAN_REVERSION,
        "atr_buffer": 1.0,
        "conditions_buy": [
            {"type": "pivot_reversal", "timeframe": "M15", "level": "support"}
        ],
        "conditions_sell": [
            {"type": "pivot_reversal", "timeframe": "M15", "level": "resistance"}
        ]
    },
    {
        "id": "ATR_Trailing_Stop_Follower",
        "desc_buy": "LuxAlgo ATR Trailing Buy. Entering long as price bounces off ATR trailing stop line.",
        "desc_sell": "LuxAlgo ATR Trailing Sell. Entering short as price rejects off ATR trailing stop line.",
        "primary_tf": "H1",
        "conf_tfs": ["H4"],
        "recommended_pairs": PAIRS_ALL_TRENDING + ["GBPAUD", "EURNZD"],
        "atr_buffer": 1.3,
        "conditions_buy": [
            {"type": "atr_trailing_bounce", "timeframe": "H1", "direction": "bullish"}
        ],
        "conditions_sell": [
            {"type": "atr_trailing_bounce", "timeframe": "H1", "direction": "bearish"}
        ]
    },
    {
        "id": "Donchian_Channel_Break",
        "desc_buy": "LuxAlgo Donchian Buy. 20-period Donchian channel upper band breakout.",
        "desc_sell": "LuxAlgo Donchian Sell. 20-period Donchian channel lower band breakdown.",
        "primary_tf": "H4",
        "conf_tfs": ["D1"],
        "recommended_pairs": ["GOLD", "USDZAR", "GBPJPY", "EURUSD"],
        "atr_buffer": 2.0, # Long term breakout needs deep stops
        "conditions_buy": [
            {"type": "donchian_breakout", "timeframe": "H4", "direction": "bullish"}
        ],
        "conditions_sell": [
            {"type": "donchian_breakout", "timeframe": "H4", "direction": "bearish"}
        ]
    },
    {
        "id": "Fibonacci_OTE",
        "desc_buy": "LuxAlgo Fibonacci OTE Buy. Pullback to 61.8 - 78.6% retracement zone in uptrend.",
        "desc_sell": "LuxAlgo Fibonacci OTE Sell. Pullback to 61.8 - 78.6% retracement zone in downtrend.",
        "primary_tf": "M15",
        "conf_tfs": ["H1"],
        "recommended_pairs": PAIRS_LIQUID_MAJORS + ["GOLD"],
        "atr_buffer": 1.1,
        "conditions_buy": [
            {"type": "market_structure", "timeframe": "H1", "direction": "up", "lookback": 50},
            {"type": "fib_ote_entry", "timeframe": "M15", "direction": "bullish"}
        ],
        "conditions_sell": [
            {"type": "market_structure", "timeframe": "H1", "direction": "down", "lookback": 50},
            {"type": "fib_ote_entry", "timeframe": "M15", "direction": "bearish"}
        ]
    }
]

with open("luxalgo_top_20_strategies.txt", "w", encoding="utf-8") as f:
    item_counter = 1
    for s in base_strategies:
        # Buy strategy
        buy_obj = [
            {
                "script": s["id"],
                "strategies": [
                    {
                        "name": f"{s['id']}_Buy",
                        "description": s["desc_buy"],
                        "direction": "BUY",
                        "primary_timeframe": s["primary_tf"],
                        "confirming_timeframes": s["conf_tfs"],
                        "min_confidence": 75,
                        "blocked_regimes": ["ranging"],
                        "recommended_pairs": s["recommended_pairs"],
                        "conditions": s["conditions_buy"],
                        "sl": {
                            "type": "swing",
                            "timeframe": s["primary_tf"],
                            "side": "low",
                            "lookback": 20,
                            "atr_buffer": s["atr_buffer"]
                        },
                        "tp": {
                            "type": "rr",
                            "rr": 2.5
                        }
                    }
                ]
            }
        ]

        f.write(f"{item_counter}. {s['id']}_Buy\n")
        f.write("```json\n")
        f.write(json.dumps(buy_obj, indent=2))
        f.write("\n```\n\n")
        item_counter += 1

        # Sell strategy
        sell_obj = [
            {
                "script": s["id"],
                "strategies": [
                    {
                        "name": f"{s['id']}_Sell",
                        "description": s["desc_sell"],
                        "direction": "SELL",
                        "primary_timeframe": s["primary_tf"],
                        "confirming_timeframes": s["conf_tfs"],
                        "min_confidence": 75,
                        "blocked_regimes": ["ranging"],
                        "recommended_pairs": s["recommended_pairs"],
                        "conditions": s["conditions_sell"],
                        "sl": {
                            "type": "swing",
                            "timeframe": s["primary_tf"],
                            "side": "high",
                            "lookback": 20,
                            "atr_buffer": s["atr_buffer"]
                        },
                        "tp": {
                            "type": "rr",
                            "rr": 2.5
                        }
                    }
                ]
            }
        ]

        f.write(f"{item_counter}. {s['id']}_Sell\n")
        f.write("```json\n")
        f.write(json.dumps(sell_obj, indent=2))
        f.write("\n```\n\n")
        item_counter += 1

print("Optimized file 'luxalgo_top_20_strategies.txt' created successfully.")
