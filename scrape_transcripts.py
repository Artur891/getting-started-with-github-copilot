import os
import time
import random
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

VIDEOS = [
    [
        "HkRVCRFzX8o",
        "How to Love Yourself Enough for the Universe to Love You Back and Give You Everything You Want"
    ],
    [
        "3nG-cttoP7o",
        "How Reality Manifestation Works. Why Some Desires Come True and Others Don't. The Reason Found"
    ],
    [
        "ofXONePpIb0",
        "This childhood trauma will ruin your life. You probably have it. But it's easily fixed"
    ],
    [
        "b47zcqcXS5w",
        "This Video Will Save You from Low Self-Esteem and a Meaningless, Miserable Life"
    ],
    [
        "ZW93s2e5uvM",
        "The Universe will test you before manifesting your desires. Fail the test? You're done for"
    ],
    [
        "pZMygIYPC2E",
        "They Took Away Our Ability to Shape Reality and Made Us Forget We Are Creators! But I’m Going to ..."
    ],
    [
        "Jl6XfEEBayQ",
        "The Ultimate Secret to Controlling Reality: High Self-Esteem and Feeling Worthy of Everything"
    ],
    [
        "l1p1WI-LVVQ",
        "Only Through Sincerity and Love for the World Will You Receive an Ideal Life from the Universe. B..."
    ],
    [
        "i1OyiWgV9PI",
        "Remove All Limits, Boundaries, and Fears. Become Infinity and Get the Best Out of Life"
    ],
    [
        "XAS_9_X3lm8",
        "All My Wishes Come True: I Hacked Reality by Giving Up on My Past Failures"
    ],
    [
        "QTDCKp4xdHM",
        "I've Solved the Main Problem With Manifesting Desires. Why Do Some Come True Easily While Others ..."
    ],
    [
        "zxuzOqv1500",
        "The Universe Will Materialize Any Desire If Your Self-Worth Allows You to Feel Deserving of It!"
    ],
    [
        "njidaD7yJCM",
        "I deliberately let life hit me hard and ended up unlocking my potential as a CREATOR. The tougher..."
    ],
    [
        "qMtQ4UCEL1Q",
        "After twenty years of suffering, I finally realized how to use the power of thought to switch to ..."
    ],
    [
        "4jgfoyYlYjY",
        "My most impossible wish came true in 12 hours. I’m convinced we live in a simulation and everythi..."
    ],
    [
        "8jth0rW_nUU",
        "Stop Taking Life So Seriously and You'll Get Everything You Want. A Universal Principle for a Goo..."
    ],
    [
        "75L9E_AbW24",
        "The Inconvenient Truth About Reality Creation: Why Losers Can't Manifest Their Desires"
    ],
    [
        "YREAamS-048",
        "The Universe Taught Me How to Control Reality. I Went Through Hell and Back to Learn This Truth"
    ],
    [
        "MOEw7YYBl4Q",
        "I figured out the secret to controlling reality. Only a few will understand, because it takes int..."
    ],
    [
        "YW4NGDBoUUQ",
        "The Biblical Method for Creating Your Best Life. Changing Reality Through the Power of Thought Is..."
    ],
    [
        "twXM1yFKEsQ",
        "I realized my thoughts control my reality and started using it to my advantage. Living my best life"
    ],
    [
        "zFPLO-8Qrv4",
        "Change Your Life With the Power of Thought in THREE MONTHS! My Magic Method! End Suffering and Cr..."
    ],
    [
        "PCHmVAVhrBI",
        "How to break the curse of poverty and loneliness. Your subconscious is creating a bad reality for..."
    ],
    [
        "MpArDc8Q_dg",
        "I Fixed the Root Cause of My Poverty and Miserable Life. How Our Subconscious Creates Our Worst Life"
    ],
    [
        "k2h0RZiR_cc",
        "The ULTIMATE SIN that blocks your manifestations and strips away your divine CREATOR power"
    ],
    [
        "Qwald6A0jcc",
        "How a Bible Quote Taught Me to Control Reality Through the Power of Thought. Manifesting Any Desire!"
    ],
    [
        "KCyr-hMiUas",
        "How I Manifested the MOST UNREAL Desires Through the Power of Thought. Our Life is a Mind Game! E..."
    ],
    [
        "daBHnrg1mo8",
        "To Live Your Best Life, You Must Drink from the Cup of Suffering to the Dregs! The Creator State ..."
    ],
    [
        "pLUMn5CQgmU",
        "How to Become Someone Loved by the Universe and Everyone Around You. A Magnetic Aura Will Give Yo..."
    ],
    [
        "0G5oyHyEebU",
        "Принятие себя и удаление чувства вины это основа трансерфинга реальности и материализации желаний"
    ],
    [
        "l9w6N5tLBjI",
        "Регуляция нервной системы это и есть соединение с Богом и материализация любых желаний"
    ],
    [
        "zb2Y6ojTsbk",
        "Living a miserable life? Energy vampires have destroyed your AURA! Toxic people and their impact ..."
    ],
    [
        "OYwXwE9jS-A",
        "Reality control according to the method of Christ. The main secret to shifting into new timelines"
    ],
    [
        "zenGKiDYsok",
        "Your life is a simulation; even if it seems terrible, you are still the master here—it’s all your..."
    ],
    [
        "ivD_WbQcT5s",
        "Christ's secret teaching on how to control reality. It always works! I get everything I want from..."
    ],
    [
        "2P6UoSsX1Hs",
        "Unlock the Power of the Creator by Overcoming Mental Limits. Manifesting Desires Requires No Effort"
    ],
    [
        "YROed4H90vA",
        "How to connect with God to fulfill all your desires and solve any problems. The only way"
    ],
    [
        "bgDYmv9-s6w",
        "To Become a God, You Must Go Beyond Fear. Unlocking the Infinite Source Within Yourself"
    ],
    [
        "3zABu5IPcVk",
        "I don't work, but God pays me just for existing. Christ's secret teaching on how not to work"
    ],
    [
        "gHEyZbgbsx4",
        "How to Lead Others with the Power of Thought. Easily Generate Sympathy and Win the Competition."
    ],
    [
        "yeRrDffKTmI",
        "Overcoming Limiting Beliefs and Manifesting Desires Through the Power of Thought"
    ],
    [
        "IhL7vXfn_IM",
        "Your logical mind is blocking your manifestations. Why your manifestation isn't working"
    ],
    [
        "RfyXNQBaLqI",
        "I Learned the Laws of the Universe, but Nearly Died Because of My Low Vibrations. My Revelation"
    ],
    [
        "LvjZKizXatM",
        "How to Finally Connect with God and Manifest Any Desire? My Method"
    ],
    [
        "eU0A5mqqcuU",
        "Как я понял что мы живем в симуляции. Как я стал избранным. Вселенная учит и выдаёт черный диплом"
    ],
    [
        "kQycwVR0ljs",
        "Nervous system regulation is the HIGHEST LEVEL of reality transurfing. In this state, anything is..."
    ],
    [
        "V6_v95iXSa0",
        "Why isn't reality transurfing working for you?"
    ],
    [
        "g4F4-tEPpsI",
        "The Biblical Key to Reality Transurfing. People Are Ignoring These Lines from the Old Testament!"
    ],
    [
        "kXZpMwvA4g4",
        "How Jesus Taught Me to Manage Reality: Connecting with Your Higher Self and Gaining Infinite Power"
    ],
    [
        "cm2IW4miDq8",
        "How a monk taught me reality transurfing. A universal law that 99% of people don't know about."
    ],
    [
        "s0Dzu1hObCg",
        "You never have to work a day in your life! The universe pays you to exist because we live in a si..."
    ],
    [
        "U2Cs1z30He8",
        "The cause of your failures and poverty has been discovered. Your mind is creating limitations for..."
    ],
    [
        "5OK_DQqtZuc",
        "The missing element of reality transurfing that no one knew about has been found! Now everything ..."
    ],
    [
        "C5PU95teX_Y",
        "The state of the Creator and reality control. Magic works. It's all achievable in just five minutes."
    ],
    [
        "vsW1vJd_sI8",
        "Breaking free from the slavery of the mind and creating a better reality"
    ],
    [
        "50Y14gY_Pyw",
        "A way out of the most difficult situations through a magical method. There are no other methods!!..."
    ],
    [
        "MpiRAiCbZi4",
        "Learn to manage your attention and you will learn to manage reality."
    ],
    [
        "gxRxeUNkqM8",
        "A MAGIC PILL for controlling the universe has been discovered. No one will tell you about it."
    ],
    [
        "csB8U-mnYZg",
        "You've forgotten that you're God, I'll remind you. Why does transurfing work? Why shouldn't you b..."
    ],
    [
        "yLA_phoHQKc",
        "How humility opens the way to a better life and the solution to all problems"
    ],
    [
        "b1gypQW-SLk",
        "What to do when your life is falling apart before your eyes?"
    ],
    [
        "Js_jIZ6dCyM",
        "The Universe responds to requests INSTANTLY. Solving ANY PROBLEM through the universal law of the..."
    ],
    [
        "_4_U7_vlO4E",
        "I created an intention in reality transurfing, but it only got worse. Why is that? There's an ans..."
    ],
    [
        "MJLyoC0rw10",
        "What to do when life is going downhill? It affects everyone."
    ],
    [
        "8UvgjpjVT1M",
        "Self-acceptance is the basis of reality transurfing and improving your life scenario."
    ],
    [
        "14hgiGoR_Vg",
        "The Main Mistake in Intention Setting: Why Reality Transurfing Isn't Working for You"
    ],
    [
        "jXGhb30w2MY",
        "Stop waiting for people to validate your worth and your life will get better."
    ],
    [
        "jy9jbB6KdL8",
        "Every moment is perfect. You've forgotten that you are the entire universe. You've created obstac..."
    ],
    [
        "zFoNp0vUif8",
        "How to break through the wall of poverty and destitution? How to become a legend in your lifetime..."
    ],
    [
        "A0hOza72pUU",
        "Reality is a projection of your internal state. Controlling the universe through changing state"
    ],
    [
        "Dsv-7hPf0JM",
        "The easiest way to convince your subconscious that your desire has ALREADY MATERIALIZED"
    ],
    [
        "DroaCER9Geo",
        "An intention is simply a thought reinforced by your energy. Any intention ALWAYS comes true, that..."
    ],
    [
        "XFbrh-WFejM",
        "How we create our own hell with the power of thought and repel others with our aura. Egregors and..."
    ],
    [
        "WwY2o9oMVWA",
        "Ты и есть ВЫСШАЯ СИЛА в этой Вселенной. Начни отдавать приказы этой реальности, ты начальник"
    ],
    [
        "mz6FowEa1Tw",
        "Managing reality using the method of Jesus Christ and more. It's so easy that any moron can under..."
    ],
    [
        "s2bB77H2JPE",
        "Transition to a better branch of reality with one simple trick. Christ's advice works always and ..."
    ],
    [
        "j4AIW8ysZxE",
        "You are the ENTIRE UNIVERSE and you can take any form. Reality is YOUR DREAM and you can control it!"
    ],
    [
        "icJPm5iPY3o",
        "A guide to creating reality with the power of thought. Just 4 steps, even a child can understand."
    ],
    [
        "hBlogJL10oY",
        "Initiation into manhood. Male and female egregore. Where do incels come from and why aren't women..."
    ],
    [
        "16a3LjHBdFg",
        "The Male and Female Egregor. Why You're Having Relationship Failures. The Spiritual Cause of Your..."
    ],
    [
        "3epYCWpARGM",
        "The universal principle that saved and radically improved my life. The principles of karma and luck."
    ],
    [
        "eorP1H6DyHA",
        "Conquer any situation with the power of thought. The highest level of reality transurfing."
    ],
    [
        "NaJd7gtJSJE",
        "Developing Your Own Aura Through the Power of Thought. Swag. Black Diploma."
    ],
    [
        "drQkOPStcKU",
        "Increasing your aura with the power of thought"
    ],
    [
        "SHj6ul7nNHg",
        "How a powerful aura is formed that attracts people and others. The power of thought creates an aura."
    ],
    [
        "NoUOj6ge_1w",
        "The key to reality transurfing is the principle of non-duality."
    ],
    [
        "EvhM81ReUu8",
        "Practice of defeating the devil and materializing your desires"
    ],
    [
        "kwXnchVow9Y",
        "Defeating the Devil and Gaining the Power of Reality Transurfing. How the Devil Disrupts Your Man..."
    ],
    [
        "rncG9e2M25o",
        "A superpower in reality transurfing. Without it, nothing will work."
    ],
    [
        "NcHOyijgPzc",
        "Твой уровень денег напрямую зависит от чувства внутренней безопасности. Притяжение денег силой мысли"
    ],
    [
        "8Q8YBeZyNu0",
        "Unblocking Money Blocks. Attracting Money with the Power of Thought"
    ],
    [
        "ABihQSamJZI",
        "Уровень твоей ауры прямо пропорционален количеству психических травм. Чем больше тем лучше"
    ],
    [
        "scF4RhzbF7k",
        "Прокачка личностной силы и ауры. Испытания и трудности это благословение от Творца"
    ],
    [
        "vdLQGjLok1E",
        "Creating a powerful magnetic aura. Personal power attracts abundance into our reality."
    ],
    [
        "jCaQaT3aaWQ",
        "Your level of income depends on your inner world. Rich thinking and abundant reality"
    ],
    [
        "-O5REoE2Xoo",
        "Women don't like kind and good men. They always cheat on them :("
    ],
    [
        "JQoVarz-3vw",
        "The Psychology of Appearance. How a Beautiful Appearance Forgives You All Your Sins and Opens All..."
    ],
    [
        "kCPQjNokrTg",
        "The most beautiful trait of a person that immediately attracts the attention of others"
    ],
    [
        "bDnp-aHwmW8",
        "The difference between a loser and someone who succeeds in everything! The difference lies in one..."
    ],
    [
        "0G-nn5AkgnA",
        "Rewrite your life's script with the power of thought, even when things are going badly. The effec..."
    ],
    [
        "zrUK_yWhd5Q",
        "Отличие Бога от раба. Почему ты живёшь так плохо. Главная ошибка которую тебе внушили религиозники"
    ],
    [
        "qbxxI1GUse8",
        "I Realized the Horror of My Life and Became a Top Blogger. From Rags to Riches"
    ],
    [
        "5jpiTgVeWWE",
        "How to rewrite your life's script even when you're completely fucked"
    ],
    [
        "EfZCIXhBSVE",
        "I found the MOST IMPORTANT human quality without which you will have nothing in life!"
    ],
    [
        "H9vacwvCqVQ",
        "Психология инцелов и женская гипергамия. Почему инцел не имеет никаких шансов с женщинами"
    ],
    [
        "JqodUO4e2mw",
        "Психология инцелов. Тебе не помогут курсы по пикапу. Чего реально хотят женщины?"
    ],
    [
        "lT5wufHdkGI",
        "The psychology of incels. Why you'll never get a girlfriend if you're an incel. Who do women love?"
    ],
    [
        "SFnrna90tIE",
        "Attracting people by creating a powerful magnetic aura. The power of thought solves everything."
    ],
    [
        "7GgvEosxlt8",
        "Managing reality through releasing fears. Creating a powerful aura. Higher reality transurfing."
    ],
    [
        "IX36CuSS0CU",
        "Managing reality through de-emphasizing importance. The highest level of transurfing."
    ],
    [
        "eEI4OeZQpR0",
        "How overestimating importance destroys the materialization of desires. Without this knowledge, tr..."
    ],
    [
        "M8milEoGrWA",
        "Трансерфинг реальности и отношения. Сила мысли сама создает тебе партнера. Привороты не работают"
    ],
    [
        "i4FCqmRUsHs",
        "How we choose our own reality with the power of thought. Or how pendulums choose for us…"
    ],
    [
        "nhhlku9V2QY",
        "Treatment of alenism and cuckoldism with cold water"
    ],
    [
        "F4ss5wfL0ks",
        "Transurfing only works when the importance is zero. How can I lower the importance? Realize it's ..."
    ],
    [
        "h8yhd0GFkqA",
        "Escape the slavery of 3D reality. Life is just a simulation, and you are its master (or slave)."
    ],
    [
        "VQQhuuWmYx8",
        "You are either a slave to this reality or a master of this reality. There is no third option."
    ],
    [
        "S0Zmufg4o2Y",
        "You will never see fear in me in your life."
    ],
    [
        "vSkMoWEuUZw",
        "Proof that we live in a simulation and there's nothing to fear. Life is a dream, there's only con..."
    ],
    [
        "FhmPm2HcRjM",
        "There is no fear. There is nothing at all except your consciousness. The world is an illusion."
    ],
    [
        "OzLSYKYKyKo",
        "Don't let 3D reality control you. Be an observer and a CREATOR, not a victim of \"reality.\""
    ],
    [
        "_89rPKJbRjU",
        "There is ONLY consciousness! Enemies and problems do not exist. Fears are an illusion. There is o..."
    ],
    [
        "9PHkwXQ8-z0",
        "The power of the here and now. The creation of reality is happening now. There is nothing but thi..."
    ],
    [
        "P4r4PTnWMtE",
        "The whole essence of reality transurfing and the power of thought. Stop believing in nonsense and..."
    ],
    [
        "9XkknLWj18c",
        "The true meaning of manifestation and reality transurfing. You have been deceived and misled."
    ],
    [
        "O8yhpYR4c4w",
        "Sublimation of sexual energy and regulation of the nervous system"
    ],
    [
        "0qxF6JfKzw4",
        "All the problems come from the fact that women don't give"
    ],
    [
        "dXixT2u1wNw",
        "Controlling reality with the power of thought? The only secret people don't understand. Abiding i..."
    ],
    [
        "90O4RDdqcJQ",
        "The Most Disgusting Trait in a Man. Part 2"
    ],
    [
        "0J_e3xaEv9Y",
        "Healing bad habits with the power of thought. It's very simple, stop complicating it."
    ],
    [
        "AHA_hBpwCaE",
        "The most disgusting trait in a man: Instant loss of respect."
    ],
    [
        "Mjj-hC5CBz0",
        "My Experience Improving My Appearance: An Anti-Aging Protocol"
    ],
    [
        "onyQB-NO13A",
        "The solution to any problem is NON-RESISTANCE! A universal law that no one uses."
    ],
    [
        "2Ud2cMmk7-I",
        "This parable changed my life! No need to wait for happiness, it's already here!"
    ],
    [
        "lEqO5RI7Qqc",
        "High vibrations attract high-ranking people into your life. My experience. Vibrations decide ever..."
    ],
    [
        "_Mlghyu3EOY",
        "The Biblical Secret of Manipulating Reality with the Power of Thought. The End of Torment"
    ],
    [
        "zDYlEuRCARA",
        "How to be God above all problems. We're in a simulation and there's nothing to fear."
    ],
    [
        "fydrlylaQtY",
        "Solving financial problems with the power of thought. Reality transurfing you didn't know about."
    ],
    [
        "9zfia5_ixoQ",
        "Creating an intention and transitioning to a new branch of reality with the power of thought. It'..."
    ],
    [
        "VEGmocRb0Bc",
        "Choosing the right reality through working with the subconscious. The main principle of reprogram..."
    ],
    [
        "SYApncngQUk",
        "How we choose our own path to reality from an infinite number of potentials. You can do anything!"
    ],
    [
        "D0FyCQc9Vu8",
        "We live in a simulation and we control it ourselves, but you don't even suspect it. Anything is p..."
    ],
    [
        "i8Qquai7xWM",
        "Healing illnesses and improving your appearance with the power of thought. My experience. Reality..."
    ],
    [
        "UkBS-dDkcus",
        "Poverty is a lifelong curse. My experience"
    ],
    [
        "iM71G1X3q1k",
        "How reality reacts to our vibrations. Creating the right vibrations for a new reality."
    ],
    [
        "DlG--gFNUvs",
        "Our reality is a simulation. How can we control this simulation? Scientific evidence."
    ],
    [
        "x6Q_hpUAhko",
        "The key principle of reality transurfing. Without it, it won't work. My experience of dream mater..."
    ],
    [
        "hrGL9HY00JU",
        "Escape from slavery into CREATOR MODE. Start managing reality, or it will manage you."
    ],
    [
        "-Wxr9Kxn6-Y",
        "To materialize the desired reality, you need to step over the EGO and become a CREATOR"
    ],
    [
        "U1YdwkXmOK0",
        "You live in a simulation. You control this simulation. You create difficulties in this simulation."
    ],
    [
        "I-BrNssGzTw",
        "How to influence people with the POWER OF THOUGHT and your vibrations? My simple method always wo..."
    ],
    [
        "kWdqniUpTAk",
        "How to be God and control your reality? It's simple! You are already God and always have been."
    ],
    [
        "GA7xcbi4bqc",
        "The Universe ALWAYS fulfills your intention for success. My story: Our beliefs shape reality."
    ],
    [
        "MGDRlAd7280",
        "How to change people's attitudes toward you with the power of thought. Your vibrations always spe..."
    ],
    [
        "IxKhK4tjULk",
        "The only CORRECT METHOD of prayer to get what you want. Your prayers never work."
    ],
    [
        "85s29z9zMWg",
        "My method for creating an abundant life through the right vibrations and sensations. A new versio..."
    ],
    [
        "b2uiYdAGL_0",
        "God Mode and the Creation of ANY REALITY! How to Control Our Simulation? The Universe Revealed a ..."
    ],
    [
        "C0j-Rsk1qcg",
        "How I quit my job thanks to reality transurfing. We create any reality we want."
    ],
    [
        "gUAKNozpR0I",
        "Avoid women like that at all costs. The new red flag everyone's keeping quiet about."
    ],
    [
        "cH4wmM-l00o",
        "How we voluntarily manifest a bad reality for ourselves. But we can do the opposite."
    ],
    [
        "sKaLWdO_u20",
        "I eat ONLY RAW MEAT. Is it the best diet in the world? I'll try it myself."
    ],
    [
        "5QJ_di4PdOA",
        "How I learned reality transurfing and thought materialization in prison. It's all so easy, really."
    ],
    [
        "H1oMGJCnc3o",
        "Materialization of thoughts is not magic, but a UNIVERSAL LAW. My method for creating a good real..."
    ],
    [
        "KwqO4z-5S_k",
        "The only formula for materializing thoughts. You've already materialized so much bad stuff using ..."
    ],
    [
        "atq832fTMiA",
        "Creating the desired reality with the power of thought is so easy that it becomes ridiculous. You..."
    ],
    [
        "E8gdAhml6RA",
        "A simple explanation of how to transition to better branches of reality. Universal law and the su..."
    ],
    [
        "pE-g6XZCCRE",
        "A cool method for creating the reality you want. How the Universe works and how to use it to your..."
    ],
    [
        "Xp6bTH_Tkuc",
        "What's stopping you from moving into your desired reality? Unconscious limitations that need to b..."
    ],
    [
        "9RQHfmYqbSc",
        "Be careful with your thoughts, because they always come true. The universal law always works."
    ],
    [
        "IdF-I5ecDKI",
        "Manifesting desires is so easy that it becomes boring."
    ],
    [
        "2Z8ZiJ0iguE",
        "I'm already tired of talking about the materialization of desires, but I'll tell it again so that..."
    ],
    [
        "E1GMoHllg2Y",
        "Transition to abundance and wealth without doing anything. Receive hints from the Universe for free."
    ],
    [
        "oo8dna49cpg",
        "Transitioning to an abundant branch of reality using the simplest method. Nervous system programm..."
    ],
    [
        "mjyvxICYPsM",
        "Transform any pain into success and wealth. Change reality with the snap of a finger."
    ],
    [
        "vDP80FQvQq8",
        "Reasons for Failures in Reality Transurfing. The Collective Unconscious. Psychoanalysis"
    ],
    [
        "FzznO37XH6k",
        "Proof that we live in a simulation and you yourself are the Creator of this simulation."
    ],
    [
        "VFML4-dv94E",
        "The transition to a new branch of reality occurs as soon as you perform this action. It's simple"
    ],
    [
        "Rju_5tzVwzk",
        "Bringing back your ex with the power of thought? It works, but there's a catch. Reality Transurfi..."
    ],
    [
        "hUEq0LE-zj0",
        "The basis for transitioning to the desired branch of reality. Without this, it is impossible to m..."
    ],
    [
        "e6cqmg-29JY",
        "Select ANY BRANCH OF REALITY through the simplest formula. Cheat codes for the Universe and the s..."
    ],
    [
        "RIWK_v0Npyo",
        "We live in a simulation, and it's very easy to transition to the desired reality. Biblical evidence"
    ],
    [
        "09JWOaRkgJQ",
        "Proof That We Live in a Simulation and Anything You Want Is Possible Here"
    ],
    [
        "cpw7XEonH7M",
        "Вселенский закон определяющий твою привлекательность и магнетизм"
    ],
    [
        "Dd4l-ctIcrI",
        "Без этого качества невозможно привлечь женский пол"
    ],
    [
        "IrrxgOCYydk",
        "Как женщина уничтожит твою самооценку и выплюнет тебя как биомусор"
    ],
    [
        "sTTMoQusEbA",
        "Почему твои отношения заканчиваются даже не начавшись? Первобытные триггеры привлекательности"
    ],
    [
        "Z4DuIP90OFk",
        "Choose any branch of reality and be reborn in literally one second. It's very simple."
    ],
    [
        "7IG4th7w_d8",
        "Ушел в отшельничество в 28 лет и это было ЛУЧШЕЕ РЕШЕНИЕ"
    ],
    [
        "aBsxt0is6TM",
        "I went into seclusion at age 28. I'm starting a fast like Jesus in the desert. Developing superpo..."
    ],
    [
        "p86jH1oV6Iw",
        "Почему 90 процентов отношений заканчиваются в первый месяц. Главный триггер привлекательности"
    ],
    [
        "ggSd4_qChzo",
        "Переход на ЛЮБУЮ ВЕТКУ РЕАЛЬНОСТИ абсолютно без усилий . Это так легко что кажется магией"
    ],
    [
        "lX-Bgf37jKw",
        "Переход на любую ветку реальности за секунду. Как собственные убеждения создают жизненный сценарий"
    ],
    [
        "LLl6vyeOIyo",
        "Beyond 3D Reality. You Are Immortal, You Just Forgot. Withdraw Your Attention from 3D"
    ],
    [
        "bz6qZAjamAs",
        "There's nothing you need to do here; everything is attracted to you. The Biblical Secret of Manif..."
    ],
    [
        "Kj5HLAaeANU",
        "Are you manifesting your desired reality, but things are only getting worse? This is NORMAL!"
    ],
    [
        "IxwItbfNPcg",
        "Желания материализуются легко, но могут принести МНОГО ПРОБЛЕМ. Избегай мою ошибку"
    ],
    [
        "kcRO60QRXpw",
        "I understood the Universal Law and went into seclusion. The Law of High Vibrations is described i..."
    ],
    [
        "1U_gohw0N4s",
        "You control this universe. You choose your own destiny. I chose the destiny of a winner."
    ],
    [
        "pewIB7KVauI",
        "Ничего в жизни не хотеть ЭТО ВЫСШИЙ УРОВАНЬ ВИБРАЦИЙ который даст тебе всё о чем ты даже не просил"
    ],
    [
        "Md1jMWVDm5k",
        "Conquering your fears gives you a powerful aura and the ability to create reality. The main secre..."
    ],
    [
        "9iuB6TCa5Gs",
        "Fear Nothing in This Life and the Universe Will Give You Everything You Never Even Asked For"
    ],
    [
        "q17OZ-66K5w",
        "Любовь к себе создает мощнейшую энергетику и люди вокруг это чувствуют"
    ],
    [
        "RnuHzioqYHw",
        "Прошлое можно ПЕРЕПИСАТЬ и создать новое будущее. Управление вниманием и создание новой реальности"
    ],
    [
        "qqm8dMoNmVs",
        "Два года полового воздержания сделают из тебя человека. Женщины сами начнут бегать за тобой"
    ],
    [
        "4Ax12yqSC8k",
        "Nothing Is More Important Than Your Vibrations. Your Only Goal In Life Is To Maintain High Vibrat..."
    ],
    [
        "VUztt6BSrsU",
        "Психологии отношений не существует. Любые отношения это просто обмен вибрациями"
    ],
    [
        "ynUGEdG8Y1I",
        "Как создать себе ауру которая будет притягивать в жизнь самые лучшие события. Закон вибраций"
    ],
    [
        "jLaTXkhaouc",
        "The Only Way to Solve Any Life Problem Is by Changing Your Vibrations and Emotional State"
    ],
    [
        "fYuZO4NEa6g",
        "Changing reality by changing the emotional background. Emotion is the basis of reality transurfing."
    ],
    [
        "NL54ngpkDs8",
        "Как создать вибрации которые притянут в твою жизнь самые лучшие события. Откуда берутся вибрации"
    ],
    [
        "eVM6t5FwvEg",
        "Taking Control of This Universe Using One Simple Trick. Changing Your Reality"
    ],
    [
        "6htcvCfzXdQ",
        "Accepting death and ignoring reality is the key to high vibrations and creating a better destiny."
    ],
    [
        "vSFjc_KR918",
        "Я научу тебя игнорировать реальность что сама Вселенная пошатнётся от твоей крутости и силы"
    ],
    [
        "TPEU6Kf87qQ",
        "Вселенная имеет женское начало. Кто понял женщину- тот понял как функционирует наша реальность"
    ],
    [
        "fKAa5ETngI4",
        "Пойми что времени не существует, это просто иллюзия твоего разума. Манифестация моментальна"
    ],
    [
        "FXFT4X3bRzo",
        "How Jesus taught us to TRANSSURF REALITY and create our own life scenario"
    ],
    [
        "iUeL_crT3Qo",
        "Чтобы творить нужную реальность пойми что времени не существует и манифестация МОМЕНТАЛЬНА!"
    ],
    [
        "2jNpgy_nTX8",
        "Relationships Between Men and Women Are an Exchange of Energy and Vibrations. Relationship Psycho..."
    ],
    [
        "L5qz6VfJOu0",
        "Я докажу что ты ТВОРЕЦ СВОЕЙ РЕАЛЬНОСТИ за 25 минут. Почему мысли материальны и что с этим делать"
    ],
    [
        "QtPLyf_Kh20",
        "Why studying relationship psychology will ruin your life. There's another way to build relationsh..."
    ],
    [
        "-J9NM70uuiU",
        "Желание не материализуется пока ты его ждешь. Не жди, а просто позволь ему быть"
    ],
    [
        "D7y9-sLzCO8",
        "Ignoring reality is the CREATOR MODE when you can materialize whatever you want!"
    ],
    [
        "wAq-9H5taIo",
        "The Universe revealed the secret of controlling reality to me. I feel like a prophet"
    ],
    [
        "B96q5p-l9v0",
        "Причина всех твоих неудач в тебе. Негативные установки отражаются в реальность всегда без исключений"
    ],
    [
        "gwU-UbcHHsc",
        "Because of this error in REALITY TRANSSURFING I was unable to materialize anything"
    ],
    [
        "ynViZQRgajc",
        "Девушка НИКОГДА не забудет эту фразу от тебя. Способ контроля отношений и занятия сильной позиции"
    ],
    [
        "H-3UFiKPtIE",
        "Ты бегаешь за девушкой и унижаешься? Это скрытый гомосексуализм! Психология о которой вы не знали"
    ],
    [
        "XXOX0vwjAOk",
        "Люди с тяжелым прошлым очень талантливы в трансерфинге реальности. Секрет создания нужной реальности"
    ],
    [
        "j719Vpikhp4",
        "Why does the law of tithing work? Giving money to charity always results in more in return."
    ],
    [
        "MSf7eYUBdoM",
        "Вся правда про мужскую ауру которая так нравится женщинам"
    ],
    [
        "_jwP0UrMLHQ",
        "Пустота внутри  и пустота в глазах. Что с этим делать, как себя воскресить и начать жить?"
    ],
    [
        "TrL-hqPukEA",
        "Женщина мечтает чтобы над ней доминировали. Психология отношений"
    ],
    [
        "GAWEclWzdYU",
        "Are you pining for your ex? Then you deserve the worst life possible. Male energy and attraction"
    ],
    [
        "24oTpLi0pEM",
        "Хватит учить психологию отношений. Учи  ТРАНСЕРФИНГ РЕАЛЬНОСТИ и создашь  нормальные отношения"
    ],
    [
        "ayoxqDVxzlI",
        "Я настолько тупой, что не понял ТРАНСЕРФИНГ РЕАЛЬНОСТИ с первого раза, но это ведь так просто"
    ],
    [
        "V11rmWeeqFU",
        "In the beginning, there was no word, but INTENTION! The secret of Transurfing from the Bible will..."
    ],
    [
        "gfUTK3I2tVQ",
        "I learned the secret of reality transurfing on American YouTube! Nobody talks about it in Russian!"
    ],
    [
        "nTqd-EwAncw",
        "A girl quickly loses interest if you don't know this BASIC, but I'll teach you. Relationship Psyc..."
    ],
    [
        "epl7SFIoGAU",
        "Хотел вернуть бывшую, а стал тренером по  ТРАНСЕРФИНГУ РЕАЛЬНОСТИ. Слава Богу бывшую так и не вернул"
    ],
    [
        "n_idLWlzHnU",
        "Девушки любят ушами, а я люблю рассказывать им сказки. Психология отношений"
    ],
    [
        "rWSTGo_wKcM",
        "Спустя три года я понял ТРАНСЕРФИНГ РЕАЛЬНОСТИ полностью. Это настолько просто что трудно поверить"
    ],
    [
        "dX-dIL9F2S8",
        "Бесы мешают материализовать желания. Их задача забрать твоё внимание"
    ],
    [
        "4sHQ89Ahnyo",
        "My thoughts materialized in 20 minutes. Manifesting desires is even easier than breathing"
    ],
    [
        "gympz76dLs4",
        "Принятие смерти даёт тебе божественную ауру, сильнейшую энергетику и харизму. Новый уровень бытия"
    ],
    [
        "-V7UIsxcbZo",
        "Плохие люди забирают твои грехи на себя и очищают твою карму, делая твою жизнь лучше"
    ],
    [
        "i61GUuFIV4s",
        "How I embraced death and conquered this life. A new level of existence."
    ],
    [
        "GgJdFeHKL-A",
        "Что же такое «уверенность» которую женщина так ищет в мужчине? Это не то о чем вы думали"
    ],
    [
        "dHdcHn2rVRA",
        "Тяжелый труд не принесет тебе результат. Мотиваторы вас обманули. Я дам подсказку"
    ],
    [
        "2V1oGnoYNR8",
        "Самопрограммирование на высокие вибрации и успех"
    ],
    [
        "Mac6TcyT9Z8",
        "Мужская энергия которую женщина ищет в тебе. Без этого отношений не будет"
    ],
    [
        "32ciF42EDHE",
        "Вокруг много бесов в образе людей. Они хотят понизить твои вибрации"
    ],
    [
        "fyaRLe7Pw6w",
        "The reason relationships fail is because you feel empty inside. No one wants to fill that void."
    ],
    [
        "cqNiAIb8CN4",
        "После этого ты поверишь в трансерфинг реальности! Хватит мелочиться и начни уже творить что хочешь!"
    ],
    [
        "nSetGDOd-a4",
        "You are the Creator in this life, you cannot die and suffer, create any scenario for your life"
    ],
    [
        "tWwZlnAVvL4",
        "Я в шоке. Желания материализуются за три дня. Я даже ничего не делаю для этого. Трансерфинг рулит!"
    ],
    [
        "QZSWzv7EwQc",
        "Women Seek ONLY ONE QUALITY in Men! And It’s Not Money! Why You Always Get Dumped"
    ],
    [
        "afUxC_fNIl4",
        "Choosing Your Life Script by Redirecting Your Attention. Reality Transurfing in Simple Terms"
    ],
    [
        "eeYgHFYN2dw",
        "You must date multiple girls at the same time! If you want to be successful in a relationship."
    ],
    [
        "cxlAAeugDDQ",
        "Девушка любит только того кого сложно заменить. Если ты легкозаменяемый то др*чи в кулачок"
    ],
    [
        "zBteSoSLwAs",
        "Люди будут кайфовать от твоей энергетики. Твоя аура притянет в твою жизнь самое лучшее"
    ],
    [
        "A01sf8z0efI",
        "I made my dream life a reality even though I was MENTALLY RETARDED! If I could do it, you can too!"
    ],
    [
        "wpMuyIUmA7M",
        "Your ego prevents your desires from materializing. Shut up your ego and you will gain the SUPERPO..."
    ],
    [
        "LKd6nYoVwzM",
        "To mold ANY REALITY as if from plasticine. The power of thought and vibration create all events i..."
    ],
    [
        "O4El9xNu-I4",
        "Девушка влюбляется только в твою МУЖСКУЮ АУРУ. А откуда эта аура берется?"
    ],
    [
        "XLHXvXZWNxk",
        "Девушка влюбляется в твою МУЖСКУЮ АУРУ. Теряешь ауру- она перестает тебя любить"
    ],
    [
        "TGt14-95iAA",
        "The universe will return to you everything that was taken from you! Proof of God's existence! My ..."
    ],
    [
        "XR-rb227iUQ",
        "Наша реальность НЕРЕАЛЬНА! Это просто картинка созданная нами! Перестань воспринимать её всерьез!"
    ],
    [
        "u4_qvW5FEzA",
        "Материализация отношений с противоположным полом силой мысли. Трансерфинг о котором вы не знали!"
    ],
    [
        "UirE27ERZ3Q",
        "Девушка влюбляется только в твою МУЖСКУЮ АУРУ. Всё остальное неважно. Высшая психология отношений"
    ],
    [
        "pqpQsI4qPv0",
        "Эта ошибка не позволяет МАТЕРИАЛИЗОВАТЬ ЖЕЛАНИЯ. Моё главное открытие в трансёрфинге реальности"
    ],
    [
        "qaQV52voiBQ",
        "The only way to keep a girl in a relationship. 99% of men can't do that. Higher psychology."
    ],
    [
        "xjXTR_HUmG0",
        "The UNIVERSE will pull you out of any problem and make you rich. But there's one condition..."
    ],
    [
        "qtE0FFPINfQ",
        "Ты что даришь ей цветы?? Она даёт мне в первый день и умоляет остаться до утра. Психология отношений"
    ],
    [
        "KBwIAy9SSjY",
        "Единственная правильная схема отношений с девушкой. Почему тебя все бросают?"
    ],
    [
        "gnz68_zXyVk",
        "Have you forgotten you're living in a simulation? Relax, there are no problems here, and wishes c..."
    ],
    [
        "iqLozkt0_70",
        "My method for MATERIALIZING DESIRES. It works 100% of the time. Reality transurfing at its finest!"
    ],
    [
        "yUDXCospf6g",
        "The law of tithing makes you rich very quickly. The most important UNIVERSAL LAW. Freedom from fa..."
    ],
    [
        "40XQJ4fMxR0",
        "Я не оставляю Вселенной выбора кроме как дать мне САМУЮ ЛУЧШУЮ ЖИЗНЬ. Принцип управления судьбой!"
    ],
    [
        "xTKhgmP5pJw",
        "Manifesting your desires requires no effort. Stop thinking it's difficult, and everything will wo..."
    ],
    [
        "L0bzXRkaRBo",
        "Чтобы влюбиться девушка должна бояться тебя потерять. ГЛАВНЫЙ СЕКРЕТ женщин! Её страх это твоя сила!"
    ],
    [
        "4rSCswrN98U",
        "Единственный правильный формат общения с девушкой. Почему тебя всегда бросают. Высшая психология"
    ],
    [
        "YeYpA89mZGw",
        "Желания исполняются только на ВЫСОКИХ ВИБРАЦИЯХ. Главный секрет трансерфинга реальности"
    ],
    [
        "_PJXin1HT9I",
        "Самый СТРАШНЫЙ возраст для мужчины. Не совершай эту ошибку"
    ],
    [
        "LU48bAs7BK4",
        "The Only Way to Build a Relationship in 2025! There Are No Other Options! Relationship Psychology"
    ],
    [
        "gdsnlm-CMPA",
        "Never chase girls. They give to those who don't chase them."
    ],
    [
        "C-85J0RS0So",
        "Every girl is suitable for a relationship, but there's one catch! Higher psychology"
    ],
    [
        "_Gr13ZCprHU",
        "Relationship problems with your girlfriend? \"Radio Silence\" always helps! Higher relationship psy..."
    ],
    [
        "iG5wgJhftyU",
        "Стань неуязвимым к женским манипуляциям! Тебя будут хотеть все девушки! Высшая психология отношений!"
    ],
    [
        "a-UZl2R91rs",
        "Wishes materialize IN ONE NIGHT! Just eliminate one mistake and EVERYTHING WILL WORK OUT! Transur..."
    ],
    [
        "Wn29WdVWroA",
        "Общение с быдлом понижает твои вибрации и лишает удачи. Как работает энергетический обмен. Совок зло"
    ],
    [
        "5KGeapsiqx8",
        "Это ускорит МАТЕРИАЛИЗАЦИЮ ЖЕЛАНИЙ в 10 раз! Трансерфинг реальности на максимум!"
    ],
    [
        "NPOPLU0tHH0",
        "You forgot you were living in a SIMULATION and created a bad life for yourself. Reality Transurfi..."
    ],
    [
        "gkcm-ceJg74",
        "Девушка влюбляется в твой образ который создается у неё в голове. Психология отношений"
    ],
    [
        "oPYhViJN26M",
        "Главная ошибка в отношениях! Никогда не извиняйся перед девушкой, это унизительно. Высшая психология"
    ],
    [
        "GiQcGnrmxW0",
        "Unfollow ALL THE GIRLS on Instagram! Stop embarrassing yourself! The Ultimate Psychology of Relat..."
    ],
    [
        "DNw3Pe1s3LE",
        "НИКОГДА не дари ПОДАРКИ девушкам, если не хочешь разрушить ваши отношения! Высшая психология"
    ],
    [
        "0w4TaB4EdNo",
        "Find God within yourself and manifest any desire? It's very easy! Reality Transurfing works."
    ],
    [
        "_K8-ddr5Yls",
        "Почему женщины всегда устраивают проверки в отношениях? Лучшее объяснение психологии отношений"
    ],
    [
        "CRd23NGaB3U",
        "Получать важнейшие подсказки от Вселенной очень легко. Подключение к божественному источнику знаний"
    ],
    [
        "AzRl0h5brO0",
        "Твои деньги напрямую зависят от подсознания. Вот почему ты живешь в нищете. Трансерфинг реальности"
    ],
    [
        "gtxY5P4xoNo",
        "Жизнь состоит из ограничений. Убери их чтобы желания стали воплощаться. Объяснение трансерфинга"
    ],
    [
        "VK5RaGI2sFc",
        "Поведенческие программы психики формируют твою жизнь. Либо в хорошую сторону либо в плохую"
    ],
    [
        "WXgEMO8B1Hg",
        "Unleashing charisma with the power of thought! It's so simple! Maximum attraction and magnetism"
    ],
    [
        "p7teZq2SG9U",
        "Половое воздержание. Девушки влюбляются в воздержанцев, привязываются и боятся их потерять"
    ],
    [
        "UJjQfB0aXfQ",
        "I'm shocked by this secret to manifesting desires! Everything comes true SO EASILY and effortlessly!"
    ],
    [
        "beCAzbHjTY0",
        "Manipulate reality with the power of thought. People will watch you in shock."
    ],
    [
        "Q5XaqqWDt_s",
        "How will a girl test you before a relationship? The \"Flower Sucker\" Test"
    ],
    [
        "CUM6FvGdth0",
        "A girl will always question your worth. Relationship psychology"
    ],
    [
        "HRzss_PFCIU",
        "Самый первый тест в отношениях. Девушка дистанцируется спустя месяц знакомства. Не допусти ошибку!"
    ],
    [
        "vbf8bUFQbNg",
        "Почему девушка игнорит даже когда ты ей нравишься? Они сами не понимают, но я объясню!"
    ],
    [
        "4nJkDGiyHCM",
        "Доверься миру и расслабься. Ты увидишь как всё само решится в твою пользу. Забей болт на всё"
    ],
    [
        "NdlTyPS7YuU",
        "You've forgotten that you are the Creator of your reality. Life is actually very easy."
    ],
    [
        "MCQTgTheKsc",
        "Ты застрял в режиме выживания поэтому твои желания НЕ МАТЕРИАЛИЗУЮТСЯ! Трансерфинг простыми словами"
    ],
    [
        "3SGEotDIxyo",
        "Desires materialize so easily that it seems illegal ahahaha Transurfing to the MAXIMUM!"
    ],
    [
        "47dpTkf43Yo",
        "Перестань добиваться девушек с пробегом. ЭТО УНИЗИТЕЛЬНО! Её бывший получал её абсолютно без усилий"
    ],
    [
        "AmezAB6Zs9U",
        "Ничего не хотеть это СУПЕРСИЛА которая даёт тебя ВСЁ. Трансерфинг реальности простыми словами"
    ],
    [
        "iMxkyzwcm8o",
        "Saving money for a rainy day? Then that day is bound to happen. Attracting events with the power ..."
    ],
    [
        "iJUPZacJyiw",
        "Мы Творцы реальности или просто наблюдатели? Да какая разница! Трансерфинг все равно работает всегда"
    ],
    [
        "ooM64ts2poA",
        "Научись управлять своим вниманием и жизнь станет ШИКАРНОЙ! Трансерфинг реальности простыми словами!"
    ],
    [
        "qoVV8xgB7ew",
        "Conquered the fear of death and began to LIVE. Accepting death for a happy life. Attention manage..."
    ],
    [
        "bYV4HNX3pjA",
        "Девушки любят только тех кто ИЗМЕНЯЕТ. Я мразь и я делаю что хочу, но они меня любят больше жизни"
    ],
    [
        "KWcoP70gSZQ",
        "To make life a fairy tale, learn to CONTROL YOUR ATTENTION! A universal law from the Bible!"
    ],
    [
        "FhiqfA6rvPs",
        "Кто понял жизнь, тот не спешит и не работает. Как система превратила вас в РАБОВ"
    ],
    [
        "6a6d9bnm7_Y",
        "Умение ЗАБИВАТЬ БОЛТ это главный навык в жизни! Причина всех твоих страданий!"
    ],
    [
        "ETFYI6upSW0",
        "Нищета это болезнь 21-го века. Большинство мужчин даже не смогут иметь детей из-за бедности"
    ],
    [
        "X6aywMPpYQU",
        "Когда кажется что жизнь уже потеряна ПОСМОТРИ ЭТО ВИДЕО. Никогда не поздно поменять сценарий"
    ],
    [
        "utEkN3HHNzI",
        "All my dreams come true within a week! Manifesting your wishes is VERY EASY AND FREE!"
    ],
    [
        "s5RYh0YF02k",
        "Remove the limitations in your mind and you will see how EASY it is to live! There are no barrier..."
    ],
    [
        "hONo06eJw84",
        "Бесконечный источник ИЗОБИЛИЯ внутри нас. Перестань быть мелочным и жизнь станет улучшаться!"
    ],
    [
        "8oYEKNzKTjk",
        "Мы живем в СИМУЛЯЦИИ поэтому все проблемы исчезают когда ты их отпускаешь и забиваешь болт на всё"
    ],
    [
        "i9qhLPh9hto",
        "Мы живем в симуляции и все проблемы это ИЛЛЮЗИЯ! Легкая жизнь доступна здесь и сейчас"
    ],
    [
        "aEdRNphNXVg",
        "Простейший способ потерять девушку и простейший способ её влюбить"
    ],
    [
        "lZtL2nZnxFo",
        "Вселенский закон определяющий нашу жизнь. Этот закон ВСЕГДА ИСПОЛНЯЕТСЯ!"
    ],
    [
        "QW-Lq12krk8",
        "Избавься от этого ограничения и желания начнут сбываться. Трансерфинг простыми словами"
    ],
    [
        "hTkYQ0t4los",
        "Вы сами создаете себе проблемы своей СИЛОЙ МЫСЛИ. Потом не удивляйтесь что всё так плохо"
    ],
    [
        "wwGjb7hOIB8",
        "Программирование своей удачи СИЛОЙ МЫСЛИ! Жизнь на высоких вибрациях"
    ],
    [
        "ZShaV0e9SGA",
        "Создание своей реальности это ОЧЕНЬ ПРОСТО. Ты Творец реальности. Главный принцип хорошей жизни"
    ],
    [
        "vi2FWsTC-v0",
        "Я понял почему не получалось материализовать мои желания. Ключ к трансерфингу реальности очень прост"
    ],
    [
        "5yeVIzJ5QmM",
        "The main misconception that blocks the materialization of desires! Everything is actually simpler..."
    ],
    [
        "Up_rm2AMLKU",
        "Proof that we live in a simulation. And EVERYTHING is possible here. Why does transurfing work?"
    ],
    [
        "VLZqcb0cZJ4",
        "Rewiring Negative Mindsets Made EASY. Developing Charisma Through the Power of Thought. Reality T..."
    ],
    [
        "iwt4XbYHkkk",
        "Что такое мужская аура которую так любят женщины. И откуда же она берется?"
    ],
    [
        "bAIhiF07A14",
        "How to speed up the materialization of thoughts with songs. Reality Transurfing at its best."
    ],
    [
        "2fp2Tymv50g",
        "Meeting girls makes me richer and more successful. Pickup improves my life very quickly."
    ],
    [
        "OLAonV_-h2U",
        "Как на самом деле материализовать желание? Это ОЧЕНЬ ПРОСТО. Мы и есть творцы своей реальности"
    ],
    [
        "AYePW12zUPE",
        "Our life is a SIMULATION! Therefore, desires materialize INSTANTLY!"
    ],
    [
        "85gJ5fEK9vc",
        "Насколько быстро материализуются желания? МОМЕНТАЛЬНО! Трансерфинг реальности это ОЧЕНЬ ПРОСТО!"
    ],
    [
        "KrxhVOuyzxQ",
        "Как девушка определяет твою ценность? Основы мужской привлекательности"
    ],
    [
        "FoNZAafpNBQ",
        "It's very easy to manifest desires. Your brain just refuses to believe it."
    ],
    [
        "uVMcQJovRvo",
        "Главный секрет мужской привлекательности. Девушка сама создаст в своей голове твой идеальный образ"
    ],
    [
        "7zxe0LYUvzE",
        "Я раскачал тик-ток и ютуб канал СИЛОЙ МЫСЛИ. Стал богатым просто применив трансерфинг реальности"
    ],
    [
        "JjhdRESpKUM",
        "Как тревожность полностью сломала мою жизнь. Но я в последний момент смог выкарабкаться"
    ],
    [
        "cvJRjjF147o",
        "Как перестать сомневаться в материализации желаний и разблокировать трансерфинг на максимум"
    ],
    [
        "zg9Vigd8fx8",
        "Doubts destroy the materialization of your desires. You destroy yourself. The basis of Transurfing"
    ],
    [
        "bYPS2PSE-WA",
        "The secret to success and wealth lies in your subconscious. Once I realized this, everything star..."
    ],
    [
        "s3Zc-SDeG_E",
        "Две ошибки которые разрушат твои отношения с девушкой. Мой жизненный опыт за 9 минут"
    ],
    [
        "xekQWHih3Rg",
        "Секрет поддержания высоких вибраций 24 часа в сутки. Легкая жизнь обеспечена"
    ],
    [
        "2x0yDBXx2JU",
        "Я понял что мы живём в симуляции. Бедности не существует, это просто проверка на вшивость"
    ],
    [
        "6HKlKqRfkH0",
        "I Believed My World Takes Care of Me. And It Really Started To. Simple Magic"
    ],
    [
        "egNbyLxej90",
        "I started throwing money around and started getting rich even faster. Are we living in a simulati..."
    ],
    [
        "c0SuwHbI_dY",
        "Я понял как устроена Вселенная и забыл про одиночество навсегда. Секрет идеальных отношений"
    ],
    [
        "HfEAwJwPCzg",
        "I suffered from loneliness all my life, but I was able to overcome this affliction. And here's ho..."
    ],
    [
        "y6CjIL-FJl8",
        "I was able to cheat fate and win this life. The main secret of the Universe. You'll be surprised ..."
    ],
    [
        "w4c4b0o_MzE",
        "Как формируется твой ранг? Влияние окружения и конкуренции. Мужская база"
    ],
    [
        "3GSisdAv1wo",
        "Главный ключ к материализации желаний и к легкой жизни. Бесконечная вера и полнейшая безмятежность"
    ],
    [
        "KhSrbD0YMYY",
        "Музыка помогает материализовать желания. Трансерфинг реальности на максималках"
    ],
    [
        "gBL3IKLvDBI",
        "I was a \"nice guy\" and women despised me. Then I became a jerk and they fell in love with me"
    ],
    [
        "QXRDz8V-lEA",
        "Girls love monsters and scumbags like me. They don't take nice guys seriously."
    ],
    [
        "MDYoVDE9_2Q",
        "Never trust girls. You don't know what they do behind their backs. Shocking story."
    ],
    [
        "yYH-J-TEAYw",
        "Я добился изобилия женщин в своей жизни с помощью силы мысли. Трансерфинг реальности решает всё"
    ],
    [
        "oaJkLE34Odo",
        "What is male rank really? And how can it really be raised? Testosterone doesn't solve anything."
    ],
    [
        "fBBMq-cvmhw",
        "Manifesting a desire is even easier than breathing. You just need to remove the limitations in yo..."
    ],
    [
        "aWcUIKp59_g",
        "Гордыня опускает на самое дно. СЕКРЕТ УПРАВЛЕНИЯ РЕАЛЬНОСТЬЮ в победе над гордыней"
    ],
    [
        "jXjk3aRjIqQ",
        "НИКОГДА НЕ ГОВОРИ ОБ ЭТОМ ДЕВУШКЕ! Прямой путь потерять свою значимость! Психология отношений"
    ],
    [
        "rPeaFVXgQxs",
        "Уровень женского внимания на воздержании ЗАШКАЛИВАЕТ! Они сходят с ума и не могут остановиться!"
    ],
    [
        "QThs8TDrvs4",
        "The life of your dreams is closer than it seems! It's already here!!"
    ],
    [
        "t119Ee2Hx4A",
        "Как я поднялся на ютубе и бросил работу. Большинство так не смогут. Очень тяжелый путь"
    ],
    [
        "PUV5havkb3w",
        "Ты можешь внушить своему мозгу всё что захочешь и ОН ВСЕГДА ВЕРИТ! Бесконечная сила внутри нас!"
    ],
    [
        "IsLHGoKFZl0",
        "Где искать Бога? В церкви или в себе? Я выбрал искать в себе"
    ],
    [
        "kZ2my0eiAZc",
        "Я всю жизнь искал Бога в церкви, но не нашёл. А потом нашел его в себе…"
    ],
    [
        "OUdsCIVfGFs",
        "How Self-Suggestion Can Ruin Your Life: Examples from My Experience"
    ],
    [
        "SF-_0nlsuBM",
        "Внутри нас скрыта ОГРОМНАЯ СИЛА которая создаёт нашу реальность. И ей можно УПРАВЛЯТЬ!"
    ],
    [
        "x8RK_p48ct0",
        "How Your Rank Creates Your Reality. A Low-Rank Male MUST Suffer. Internal Prohibitions"
    ],
    [
        "lcje8XTJEws",
        "Девушка видит тебя насквозь, поэтому тебе не дают. Но что именно они видят в первую очередь?"
    ],
    [
        "PzLqM_heu1A",
        "Твои амбиции без реальных действий приведут к расстройствам психики и высокой тревожности"
    ],
    [
        "WTvwo5Ya3E0",
        "Как выбрать девушку в этом больном обществе? Целостность личности"
    ],
    [
        "tVQ8vcKQa_g",
        "Главное качество чтобы влюблять женщин! Выше этого нет ничего!"
    ],
    [
        "fx5glnAiQME",
        "Жизнь мужчины это борьба с похотью и унынием. Победив это ты становишься очень богатым и удачливым"
    ],
    [
        "eY30d7DdQ5w",
        "Хочешь переспать с девушкой? Не давай ей свой инстаграм! И вот почему"
    ],
    [
        "LSEX4bZKppA",
        "Я смог обмануть эту реальность используя простейший трюк! Секрет хорошей жизни!"
    ],
    [
        "QJq5fMN5ob0",
        "The formula for making women fall in love. Why you shouldn't give compliments."
    ],
    [
        "ItA_L4l5KfM",
        "Секрет УПРАВЛЕНИЯ РЕАЛЬНОСТЬЮ описан в Новом Завете! Вселенная платит тебе за твоё спокойствие"
    ],
    [
        "UOOYHvxstJc",
        "Женщина будет тебя любить только если у тебя есть другие девушки. Главный принцип отношений"
    ],
    [
        "lS7pBa2VBp4",
        "I pretended my life was perfect and it ACTUALLY BECAME PERFECT really fast. It’s a total circus"
    ],
    [
        "sI5iRp_ZirI",
        "ЕДИНСТВЕННЫЙ комплимент который можно сделать девушке. НИКОГДА не хвали её внешность!!!"
    ],
    [
        "uY91FscZb48",
        "How to please everyone around you? The answer is very simple, but many don't understand."
    ],
    [
        "iXhnGiAwmqk",
        "Вся жизнь это ИЛЛЮЗИЯ и здесь возможно ВСЁ! Бояться тоже здесь нечего!"
    ],
    [
        "qtH0MxaT_wY",
        "Я избавился от долгов силой мысли. Приставы исчезли, они существовали только в моей голове"
    ],
    [
        "UI3-ioKjX74",
        "Жизнь прекрасна здесь и сейчас. Просто ты об этом забыл"
    ],
    [
        "QqqCTaaAhC4",
        "Фильм «Матрица» раскрыл всю суть отношений с женщинами. Но этот момент никто не понял"
    ],
    [
        "kmyEB-Ce4KQ",
        "Work is for slaves! I quit my job because I'M NOT A SLAVE! Freedom must be WON!"
    ],
    [
        "7_PZK3zvdBw",
        "Шесть ключевых шагов без которых невозможно победить эту жизнь. Это всё написано моей кровью"
    ],
    [
        "O7JhKi46cEE",
        "Life Will Punish You for a Bad Mood. Your Vibrations Determine the Quality of Your Life"
    ],
    [
        "gQgCF5kZXks",
        "What really elevates a man's status? And it's not testosterone! The secret to the ideal life!"
    ],
    [
        "Fq-F9N1Ih_4",
        "How Timati taught me to make money quick and easy! But most people won't be able to do it"
    ],
    [
        "NqHPVlP0q50",
        "How the devil keeps you in poverty and suffering"
    ],
    [
        "j4Y0C9p_Fxc",
        "Я специально усложняю жизнь чтобы стать сильнее. Голод это ключ к успеху"
    ],
    [
        "EKnZmTb7Oc4",
        "После этой книги ты бросишь порно и все зависимости. Михаил Булгаков «Морфий»"
    ],
    [
        "OdqrnUkzNYQ",
        "Girls don't need money!! They need your aura! It's that simple."
    ],
    [
        "YhkxLzMhQ28",
        "Единственный плюс США это СВОБОДА!!! Поэтому я здесь"
    ],
    [
        "8K7v8QM3nhU",
        "Is it better to live in Russia or the USA? The answer is NOWHERE!!"
    ],
    [
        "ZmmSy-ciljI",
        "Girls start loving you when you quit your job. After I quit my job, I became a magnet for women."
    ],
    [
        "Zg2pboHh-Pg",
        "Как я исцелил неизлечимую болезнь силой мысли. Сила намерения меняет жизни"
    ],
    [
        "_6XLpgxdD-k",
        "Почему меня любят все девушки? Единственный фактор которого вам не хватает"
    ],
    [
        "HB1AQtf8WPg",
        "Как челюсть влияет на твой ранг. Анатомия привлекательности"
    ],
    [
        "gSb_Vhx2z4A",
        "Черный диплом это инструкция к жизни. Это меня спасало очень много раз"
    ],
    [
        "4d9zAjYWncI",
        "Ученый раскрыл тайну всех женщин! В кого влюбляются девушки на самом деле? Основа притягательности"
    ],
    [
        "mr4BWVO_ugE",
        "The main sign of human degradation. The need for stimulation."
    ],
    [
        "1FhiQAsH-aY",
        "Как инстаграм разрушает отношения и делает тебя одиноким"
    ],
    [
        "H3ZjXEg1CRE",
        "Никогда не пиши девушкам. Это унизительно"
    ],
    [
        "YsTaAib0mNw",
        "Девушки любят отморозков. Доказательства"
    ],
    [
        "8BWNAVFX1Jc",
        "Two Causes of Depression. Why Is Life So Bad?"
    ],
    [
        "-I_s67p4uxA",
        "Who Do Girls Really Like? Double Standards of Attractiveness"
    ],
    [
        "vC44IQMI4Sk",
        "Don't let a girl judge you. Don't try to understand her."
    ],
    [
        "M_rnmRSvX5w",
        "Loneliness is a man's main enemy."
    ],
    [
        "38dKLs9rsgY",
        "Единственная правильная тактика в отношениях с девушками. Судьба женатика очень тяжелая"
    ],
    [
        "4AeZzhIFVdE",
        "Главный секрет привлекательности который никто не понимает. Состояние Творца"
    ],
    [
        "Jfpspx8JgY0",
        "I recovered from Alenism, but made another mistake. A collapse of significance and self-reflection"
    ],
    [
        "dBbu5slCnlk",
        "Главная ошибка при знакомствах с девушками. Бессознательное падение статуса"
    ],
    [
        "Yrwn-wfuxeE",
        "I will prove that thoughts are material in just 6 minutes."
    ],
    [
        "r_QlsgqSVpg",
        "Религия отделяет тебя от Бога и превращает в раба. Я встретил Бога в макдональдсе"
    ],
    [
        "QakTkdXGfqg",
        "Страх остаться без денег- это главная ловушка матрицы! Я бросил работу и не жалею!"
    ],
    [
        "48eXNnsaKmo",
        "Как я выжил в самых смертельных ситуациях. Простой дедовский способ!"
    ],
    [
        "XQgXG5lekhw",
        "Как на самом деле работает любовь? Кого девушка бросает и кого любит?"
    ],
    [
        "omA6epF3XLY",
        "Работа это грех! Крепостное право существует до сих пор!"
    ],
    [
        "dpr0oXX6RpM",
        "Going to work is humiliating. I quit my job so I wouldn't be humiliated"
    ],
    [
        "Lh36y-IDMto",
        "Демоны, лярвы и половое воздержание. Причина твоих срывов"
    ],
    [
        "QMvDjsWkFAI",
        "Сострадание это главное качество успешного человека"
    ],
    [
        "768k3FZ_FzM",
        "Fear of expressing yourself to the world limits you in everything. The only boundaries are in you..."
    ],
    [
        "QZRM_yEBy2o",
        "Жадность это главное качество нищеты. Бог это бесконечный источник"
    ],
    [
        "le8jYPmObAs",
        "Я очень боялся стареть, но психотерапевт меня спас. Страх старения это вредоносная прошивка"
    ],
    [
        "wdLlzM4pvkc",
        "I cured a client of masturbation in half an hour. Abstinence and psychotherapy"
    ],
    [
        "oxwQCCfzwN8",
        "Нищета лечится с помощью гипнотерапии. Бомжацкие прошивки в голове"
    ],
    [
        "y9eRSaHogG4",
        "Мой опыт гипнотерапии. Я был в шоке от результата"
    ],
    [
        "6tku3j4Jark",
        "Advice from a millionaire that most people won't understand"
    ],
    [
        "jxBOT8seWm8",
        "God gives grace to the humble. Humility is the foundation of reality transurfing and the fulfillm..."
    ],
    [
        "2jOszp0zxHM",
        "According to your faith, so be it to you. Be very careful with your thoughts!"
    ],
    [
        "5KG33Npi8lA",
        "Forgive yourself for everything and life will become easier. Confession to yourself"
    ],
    [
        "St1O5OoYdug",
        "Are we living in a simulation or am I going crazy?"
    ],
    [
        "AeVJ4HUjJnA",
        "Turn any situation to your advantage with the POWER OF THOUGHT! Rewrite your destiny!"
    ],
    [
        "118oMNa6fmo",
        "Women have no compassion for men. If she sees you're in pain, she'll finish you off."
    ],
    [
        "KA2ohvc_DWM",
        "My experiment in reality transurfing and why it was a success. Excess potentials interfere with e..."
    ],
    [
        "9qgrs8kQZpA",
        "Отказ от ЭГО это выход из матрицы и ключ к свободе! Жизнь без страхов и ограничений!"
    ],
    [
        "AKvG8MA3Mlk",
        "Exiting the matrix means renouncing fears. All fears are an illusion."
    ],
    [
        "cz5B18W81Fk",
        "The difference in mentality between the US and the CIS. I was shocked."
    ],
    [
        "7dU6scjqIEE",
        "Бесы блокируют материализацию желаний. Трансерфинг реальности простыми словами"
    ],
    [
        "aCNAVlZNir0",
        "Я переспал с бабой два раза и потерял всю мотивацию. Половое воздержание"
    ],
    [
        "GhwpCXrsu9o",
        "Sins block the fulfillment of desires! Reality Transurfing and the Nature of Sin"
    ],
    [
        "doh02TLR6p0",
        "Я понял секрет полового воздержания который никто не знает. Взлом матрицы"
    ],
    [
        "1pP0v5iz7_c",
        "Каждый человек талантлив и успешен, но есть один нюанс.. Сила мысли"
    ],
    [
        "SQZSQSOuM7c",
        "Детские травмы блокируют исполнение желаний. Трансерфинг и условные рефлексы"
    ],
    [
        "LSWe9Dibeo0",
        "Рэпер научил меня исполнению желаний. Сила мысли может всё"
    ],
    [
        "psz6WOkjzD4",
        "A Chechen taught me how to control reality. Thoughts can do anything!"
    ],
    [
        "op5fyIq2xno",
        "I attracted money with the power of thought. And you keep working."
    ],
    [
        "9Bnrespi6oQ",
        "Побеждаем неудачи БЛАГОТВОРИТЕЛЬНОСТЬЮ! Сила мысли решает ВСЁ!"
    ],
    [
        "1eySZ8kMiZw",
        "Желания материализуются МОМЕНТАЛЬНО!! Но есть одно но…"
    ],
    [
        "Soezx8mc4ps",
        "Важнейшее упражнение в качалке, которое никто не делает! Почему я не знал раньше!!?"
    ],
    [
        "cIs3oIHt2MQ",
        "Our brain can do anything! But we forget about it."
    ],
    [
        "ba7w2XfBdig",
        "Деградация молодого поколения. Я еще не самый тупой"
    ],
    [
        "WTQuNR9TPXk",
        "Pendulums will destroy your life. Rejecting pendulums is escaping the matrix"
    ],
    [
        "MCXsySWUiNA",
        "Мир прогнил насквозь. Патриарх на Бэнтли. Мусора крышуют барыг"
    ],
    [
        "vDUpOkJbjJA",
        "I understood all the vileness of this world thanks to this... The hypocrisy of the modern system"
    ],
    [
        "2_q50a_HNKM",
        "Кризис мужской силы. Каждое поколение слабее предыдущего"
    ],
    [
        "ODDvkBaSi_Y",
        "Кто понял жизнь- работу бросил. Советское мышление убивает"
    ],
    [
        "BYWkBp9R294",
        "Unresolved gestalts will destroy your psyche. I almost went crazy."
    ],
    [
        "6wWL_OwEjb4",
        "Почему в США так много сумасшедших?"
    ],
    [
        "NP6mxbm7Ue8",
        "Managing Psychic Energy Is Managing REALITY"
    ],
    [
        "aKDVjqQq-0Y",
        "Моя борьба со своими демонами. RIP Паша Техник"
    ],
    [
        "It2vFj0Kk3c",
        "I was homeless and washed myself in public toilets. But then I opened a business."
    ],
    [
        "Fr2rpfpkvOE",
        "My revelation about the dangers of caffeine. Panic attacks and paranoia."
    ],
    [
        "l_8pamYBaOo",
        "Быть хорошим человеком- это лучшее что ты можешь сделать в жизни"
    ],
    [
        "VArPbl44QSo",
        "I was a beast, but life taught me to be human. The most important personality change"
    ],
    [
        "mI7h4jL6Pg4",
        "The Life of an Ordinary Mortal Is Hell. It’s a Ticket to the Titanic. But There Is a Way Out"
    ],
    [
        "cCSVYNGanvo",
        "How Tinder Changed the Dating Market Forever: The Drive for Dominance"
    ],
    [
        "vCMj6P8nYOU",
        "Is Your Life Falling Apart? It’s the Best Thing That Could Happen to You"
    ],
    [
        "YGtCuKHToNc",
        "Самая привлекательная черта человека. Как стать притягательным и получать от жизни всё что захочешь"
    ],
    [
        "EsrU3L3-cpE",
        "I realized that work KILLS and quit working forever"
    ],
    [
        "if9XVpqHS7w",
        "I hated my job and quit it forever."
    ],
    [
        "0dAPsSpSXc0",
        "Дофаминовый кризис современных девушек. Отношения больше невозможны"
    ],
    [
        "s7pZg6n_ML4",
        "Старайтесь опередить друг друга в добрых делах. Всё остальное неважно"
    ],
    [
        "ueK3QoJf_sg",
        "My meeting with Jesus. After that, I stopped being afraid of death."
    ],
    [
        "bMAE0Fbm7BQ",
        "Я умылся кровью за свои грехи. И я не хочу продолжения"
    ],
    [
        "Tj06GarGSvI",
        "The Bible taught us how to understand women. The higher psychology of relationships. The main mis..."
    ],
    [
        "PTwa9rSgfu4",
        "Прямой путь к расставанию! Ты станешь ей противен после этого действия.."
    ],
    [
        "P46B05XsF6Y",
        "НИКОГДА НЕ ЗНАКОМЬСЯ С ДЕВУШКАМИ! ЭТО ВЫГЛЯДИТ УНИЗИТЕЛЬНО!"
    ],
    [
        "dLntQ00xzPw",
        "Главный чит-код на хорошую жизнь. Почему я не знал этого раньше.."
    ],
    [
        "Gs_4aMOAjUA",
        "Girls can't take their eyes off me. Sexual abstinence enhances your attractiveness."
    ],
    [
        "8Tz2PTBJctI",
        "Я понял что в жизни можно НЕ РАБОТАТЬ!! И это было лучшее открытие!"
    ],
    [
        "LTgsqTM7gYM",
        "Новый развод в интернете! Барыги угрожают убийством!!"
    ],
    [
        "6vEDoclXurk",
        "I fell in love with LIFE, and life fell in love with ME!! Happiness exists"
    ],
    [
        "v-zHeuca-8Y",
        "Прощение это ключ к БЛАГОСЛОВЕНИЯМ. Сохрани в себе человека!!"
    ],
    [
        "TqiTws8-EYg",
        "The most important divine commandment that will change your life! Why didn't I know about this be..."
    ],
    [
        "dj9cOMb75q8",
        "All your problems are NOTHING!!"
    ],
    [
        "EWv32h4SHcQ",
        "This thought saved my life! The main setting in your head that will change your reality!!"
    ],
    [
        "tG4CxcGXfTM",
        "A guy in the gym told me the biggest secret of life. I was shocked."
    ],
    [
        "Nwk2_RT_mTE",
        "The only way to GET PUMPED UP. Dopamine binding. The desire for dominance."
    ],
    [
        "X5TpRyWq-X8",
        "What Is Male Self-Development Really About? I Was So Wrong…"
    ],
    [
        "P2bSJLJzAVs",
        "Ты умрешь один. К сожалению"
    ],
    [
        "IqqyAXQ4fgs",
        "Делай то, что ранит тебя больше всего. Только так обретаешь силу"
    ],
    [
        "eofEsbzTPJg",
        "God exists! Help your neighbors and draw closer to God! My revelation"
    ],
    [
        "WR3CJvlqr_0",
        "Девушку добиться НЕВОЗМОЖНО! И вот почему…"
    ],
    [
        "YAHZQOHx4aU",
        "Девушка стала зарабатывать больше тебя? Тебе конец! Психология отношений"
    ],
    [
        "yP9nidCM6kY",
        "Женская гипергамия это СТРАШНАЯ ШТУКА! Психология отношений"
    ],
    [
        "lZNZsGUWuJ0",
        "Она боялась что я разобью ей сердце. Психология отношений"
    ],
    [
        "-io7h4jOZtc",
        "After the gym, I reflect on relationships #3: Old age alone"
    ],
    [
        "hf9FMYnxC3Y",
        "После качалки размышляю об отношениях #2 любовь это иллюзия"
    ],
    [
        "n8vgE9_DIPM",
        "После качалки размышляю об отношениях #1 любви нет"
    ],
    [
        "rbjjJnCKnH0",
        "Я научился радоваться жизни хотя раньше страдал каждый день. Мой главный урок"
    ],
    [
        "KNZyUdbC6A4",
        "Как меня «святая» девушка бросила. Психология отношений"
    ],
    [
        "xNhlmThhebk",
        "Melstroy's Main Problem: Why Money Won't Make You Happy"
    ],
    [
        "---PDwvzJYk",
        "How My Woman Left Me Because of a Song. Relationship Psychology"
    ],
    [
        "P5Vzd4eLlw8",
        "Pray for your enemies. This is the key to a better life."
    ],
    [
        "Wd4UBp0seWI",
        "Я понял почему был аленем в отношениях! Главная причина нуждаемости в женщинах!"
    ],
    [
        "tMKqEH4TNIE",
        "Я понял всю ПСИХОЛОГИЮ ОТНОШЕНИЙ благодаря Библии и Корану! Ответ очень простой!!"
    ],
    [
        "WSgI40_5toU",
        "How I Make Money Off Suckers Online! Money Falls From the Sky!"
    ],
    [
        "Se3QTTKWJow",
        "I SLEPT WITH THIRTY ESCORTS and understood female psychology!!!! You’ll be surprised!"
    ],
    [
        "-Wo6ol2HMk8",
        "Почему так трудно быть наставником в интернете? Мужские коучи не доживают до тридцати лет"
    ],
    [
        "XDSxUrEhacg",
        "My WORST sin. The root sin as the cause of all sins."
    ],
    [
        "kTtUBtdSngs",
        "A man only has ONE WAY! I almost wasted my life until I realized this!"
    ],
    [
        "HUJcJOpBXiw",
        "The most terrible female MANIPULATION! I almost hanged myself!!"
    ],
    [
        "Ck2qwAqBHz8",
        "Меня бросили 30 ДЕВУШЕК!!! И вот что я понял из этого! Главная причина расставания.."
    ],
    [
        "f1K7GrSVI_0",
        "I was living in hell!! Until I learned about pendulum theory from Vadim Zeland."
    ],
    [
        "SOKbthPSHmo",
        "Дрочка сделала моё лицо тупым и похожим на идиота!! Воздержание даёт МОДЕЛЬНОЕ ЛИЦО!!"
    ],
    [
        "S4y5lxp7kWE",
        "Как я влюбляю девушек одними словами! Даже без денег!!"
    ],
    [
        "hS4UmgZUwyA",
        "Я сходил на массаж к проститутке и жизнь поменялась навсегда!! Шокирующая история!"
    ],
    [
        "Jb0EA-xunnQ",
        "Я переспал с бабой после двух лет воздержания! Я был в шоке что со мной стало!!"
    ],
    [
        "hLM7UyB7tQg",
        "Я понял почему жил такую убогую жизнь.. после этого всё поменялось"
    ],
    [
        "96GvZy-Z6nw",
        "I realized why I lived such a shitty life! Reality transurfing you didn't know about!!"
    ],
    [
        "yS0svfainM0",
        "I quit caffeine and was shaking like a drug addict. Giving up coffee is a direct path to wealth!!"
    ],
    [
        "6xaU0i5z-_M",
        "I stopped listening to music, and I advise you to do the same. The fastest path to wealth"
    ],
    [
        "FtjieqgeK7g",
        "Единственный способ поменять жизнь и разбогатеть. Без тупой мотивации из пацанских пабликов!"
    ],
    [
        "rbsUEgVeVsA",
        "Почему ты живешь так бедно? Библейская трактовка твоей жизни нормальным языком. Высшая психология"
    ],
    [
        "kKtOkZPDm8I",
        "I'll explain how you were turned into a deer. But I'll cure you. Higher psychology of relationships."
    ],
    [
        "ewfQX6G5F-o",
        "Get male SUPER POWER in just a second! The best way to change your life without SMS or registration!"
    ],
    [
        "iTDJ-0D4qo4",
        "Простейший способ поднять уровень жизни и стать счастливым. Победа в духовной борьбе"
    ],
    [
        "tY7hI4XLIrA",
        "Этого навыка не хватает мужчинам в 21 веке!! Подумай, может у тебя тоже с этим проблемы??"
    ],
    [
        "n_Z3sjSF1_s",
        "Этого навыка не хватает человеку в эпоху интернета!! Главный социальный навык которого у тебя нет!!"
    ],
    [
        "eMgLeLBQtJU",
        "This philosophy turns my life INTO A FAIRY TALE!!! It's better than stoicism!"
    ],
    [
        "GrXGwGdrnCw",
        "That's the ONLY thing you need to ask God for. Everything else will come naturally."
    ],
    [
        "3wGsdXDABjc",
        "THE MAIN PARADOX OF THE FEMALE PSYCHE"
    ],
    [
        "h80MU7QFxFE",
        "Abstinence creates incredible attraction in girls. Attractiveness and pickup"
    ],
    [
        "zPdOspGzRkw",
        "Таким мужикам девушки дают даже если он урод!!! Психология отношений"
    ],
    [
        "WuQ0Xvx89VQ",
        "твоя нуждаемость в женщинах сделает тебя пожизненным неудачником."
    ],
    [
        "0lTMB1GygxE",
        "Единственный способ ВЛЮБИТЬ ДЕВУШКУ!!! Жаль что я не знал это раньше…"
    ],
    [
        "gQmwljR56oA",
        "This Trait Destroys Your Attractiveness to Women. Pure Repulsiveness"
    ],
    [
        "quLd3j_3Es8",
        "I was born a freak, what should I do next? My story"
    ],
    [
        "CSJpmnao8TE",
        "Девушки сходят с ума, когда ты на воздержании. Вершина мужской привлекательности"
    ],
    [
        "GTF-zFEw8KA",
        "Я десять лет изучал женщин и понял ГЛАВНЫЙ СЕКРЕТ. Психологи об этом не расскажут. Привлекательность"
    ],
    [
        "MuVQ34w0R2o",
        "The MAIN reason to make money and escape the matrix. You haven't even thought about it. Male deve..."
    ],
    [
        "a1wJ61dT6yc",
        "Watching Zubarev? Life is going to screw you over"
    ],
    [
        "OeAzKiwEfM4",
        "Ты никогда не будешь счастлив. И вот почему.."
    ],
    [
        "j4gduB2lk6I",
        "Главная причина неудач с девушками.. Психология отношений"
    ],
    [
        "P-iuouclcfc",
        "Ты никогда не поймешь божественный замысел поэтому расслабься и кайфуй"
    ],
    [
        "nN9ca2oykhc",
        "How to become SUPER ATTRACTIVE? I studied hundreds of lectures and found the only secret."
    ],
    [
        "RAc8nS9G7cI",
        "Подружись сам с собой и жизнь станет по кайфу"
    ],
    [
        "QifeC1B1nsA",
        "Я самый богатый человек на земле"
    ],
    [
        "W3AisGf_4Tw",
        "Почему бывшая возвращается после игнора? Это важно понимать"
    ],
    [
        "mrbpDjg5KaI",
        "Важнейшее отличие умного человека от глупого. Вы этого не знали :("
    ],
    [
        "HUej8_tWTB8",
        "НИКОГДА не делай первый шаг к девушке. Психология отношений"
    ],
    [
        "DQpKMDOrQcY",
        "Почему женское воспитание сломает тебе жизнь? Эмоциональный интеллект и его отсутствие"
    ],
    [
        "tpP2lAMHycE",
        "How I Overcame Anxiety and Fear: An Encounter with Jesus"
    ],
    [
        "T5MPWIot9h0",
        "Женское воспитание уничтожит тебя. Мужской подход к жизни"
    ],
    [
        "01VfPl0myNA",
        "Как я терпилой был. Алень 80-го уровня"
    ],
    [
        "s0kfxr-C6qU",
        "Этот принцип определяет твоё качество жизни. Действовать из любви или действовать из страха?"
    ],
    [
        "FLGwTJa6gok",
        "Ты воспитан мамой и бабушкой? Тебе конец…"
    ],
    [
        "7-Ch-VaHQN0",
        "Французская мафия хотела завалить меня… пришлось уехать в Америку"
    ],
    [
        "eDFGw84T7XI",
        "Pain is the medicine for healing the soul. The Prophet by Kahlil Gibran"
    ],
    [
        "GT8n3HVnS44",
        "THE ONLY SECRET TO HAPPINESS! THIS VIDEO WILL CHANGE YOUR LIFE!"
    ],
    [
        "DmQHPa0UwX8",
        "Give people gifts. This advice will help you in life... and here's why..."
    ],
    [
        "3_fv0U4lTlg",
        "Мне 27. Нет ни семьи, ни друзей, ни девушки. Полнейшее одиночество… и это КРУТО!!!"
    ],
    [
        "xeZHEnfM5hw",
        "Никогда никого не осуждай. Жизнь сама всё расставит по местам. Грех осуждения"
    ],
    [
        "VM6jfi_PSSQ",
        "God Can Change Destiny in a Day. A True Story"
    ],
    [
        "U9UPwbqTBHA",
        "Сегодня я лично поговорил с Богом... И вот что я узнал…"
    ],
    [
        "S2s4tW7uxKc",
        "Fear ruined my football career. Fears will ruin your life… Self-doubt is EVIL."
    ],
    [
        "0gxw_ugvJ5o",
        "История знакомой наркоманки :("
    ],
    [
        "7nczqdPRiqk",
        "All your problems are due to poverty and your inability to earn money. Stress kills everything hu..."
    ],
    [
        "m4jhEP4-YyA",
        "A girl will know EVERYTHING about you if she likes you. The FSB couldn't even dream of what girls..."
    ],
    [
        "BsRbsaSnNv8",
        "Женщины хотят только ЭТОГО! Мужчины даже не догадываются! Высшая психология отношений"
    ],
    [
        "Ogw4IU9UjZs",
        "Твой внешний вид определяет твою БЕЗОПАСНОСТЬ. Чем жестче внешность- тем меньше проблем в жизни"
    ],
    [
        "c69-_IYCDhg",
        "Самая СТРАШНАЯ женская манипуляция!!! 96% мужчин попадают в эту ловушку, сами того не понимая…"
    ],
    [
        "-AymFXchTgc",
        "Искусственный интеллект заменит многих рабочих. Ты потеряешь работу и что ты будешь делать?"
    ],
    [
        "cupwDvAPhp8",
        "The cause of ALL BAD HABITS! That's why you still masturbate."
    ],
    [
        "fvK8P6wK__w",
        "Пребывать в настоящем моменте- это и есть ЖИЗНЬ. Как не терять себя и всегда присутствовать? База"
    ],
    [
        "NvowvrBCoG0",
        "I'd rather DIE than remain weak!! At night in icy water! Developing my WILL resource!"
    ],
    [
        "NDDyZIr-thA",
        "Радость от жизни естественным путем. Мозг требует удовольствия и ты обязан его удовлетворять"
    ],
    [
        "RD9uqYhlJQk",
        "Кризис среднего возраста и страх старения. Как я борюсь с этим? Самый действенный способ"
    ],
    [
        "xEnMueilago",
        "I WON'T DIE A LOSER!!!!!"
    ],
    [
        "dyVvic1aVeg",
        "Want to make a girl fall in love? Learn to put on a show. The ultimate psychology of relationships."
    ],
    [
        "ji67Hv_6x-I",
        "Закончить мучения и начать райскую жизнь очень легко. Без смс и регистрации"
    ],
    [
        "AA5dXAF7xOc",
        "Эта техника поможет стать непобедимым и развить личностную силу. Жизнь мечты ближе чем кажется"
    ],
    [
        "ptGTclpUqJE",
        "Escape from the cycle of suffering. Accepting God at the lowest point of life. The highest philos..."
    ],
    [
        "-2iO9MhhADI",
        "Money is evil and a terrible sin (but only for slaves). The psychology of slavery and the history..."
    ],
    [
        "ldbfWRoOVnw",
        "APPEARANCE IS EVERYTHING! BLACKPILL AND LUXMAXING WILL CHANGE YOUR LIFE! Higher Psychology"
    ],
    [
        "FrmGf8IZOXg",
        "Закон поддержания высоких вибраций и связи с Творцом. Те кто это игнорируют будут жить плохо"
    ],
    [
        "LaAlEZWwXEI",
        "Бью себе по лицу чтобы нарастить скулы. НЕ ПОВТОРЯТЬ, ОПАСНО! #бонсмашинг #луксмаксинг"
    ],
    [
        "biDAcpUMBWQ",
        "Developing charisma and making women fall in love is VERY EASY. The energy of ease and attractive..."
    ],
    [
        "iwsCWJbZK6s",
        "Как получить подтянутое лицо. Основа блэкпилла и луксмаксинга"
    ],
    [
        "i6BQLok3Bmc",
        "I have committed so many sins that I am obliged to do only good for the rest of my life."
    ],
    [
        "7LIF_ploENI",
        "Take up your crosses and follow me. The formula for courage. Fearlessness."
    ],
    [
        "hDH0C-hfXNM",
        "The more I gave, the richer I became. My story"
    ],
    [
        "ImqY39ucipQ",
        "Я чуть не умер, но психоаналитика спасла меня! Эти знания спасут и вас!"
    ],
    [
        "x0LtRBjhcoo",
        "Чувство вины сделает тебя нищим, больным и уродливым. Психоаналитика простыми словами"
    ],
    [
        "nXeRS5ER6Rk",
        "Эти советы от миллионера поменяли мою жизнь к лучшему. Только так побеждают"
    ],
    [
        "ficSk8izQEY",
        "Как я залип на девушку и как это выглядит смешно и позорно. Мышление неудачника. Психология"
    ],
    [
        "lBntbKqLev0",
        "Не пытайся угодить людям! Это математически невозможно! Забей болт и живи в кайф! Высшая психология"
    ],
    [
        "tKk8T8oEHfg",
        "4 явных свидетельства Иисуса из моей жизни. ЧИСТЕЙШАЯ ПРАВДА! Доказательство христианской веры"
    ],
    [
        "y2YRoKE_K2Q",
        "Детские травмы сделают тебя ОЧЕНЬ БОГАТЫМ и непобедимым(при правильном подходе). Психология личности"
    ],
    [
        "4G2dv2bsIUI",
        "Как я решил уйти с работы и начать работать на себя. Как работает карма в бизнесе?"
    ],
    [
        "07dLZSQuwf0",
        "Childhood trauma will make you lonely FOR LIFE. Personality psychology. The well-fed will not und..."
    ],
    [
        "nkeusWYzri4",
        "The position of your tongue determines your APPEARANCE. What is mewing and how to do it correctly?"
    ],
    [
        "yKiop9cVObc",
        "Поменял внутреннее состояние и  резко БОГАТЕТЬ. Жизнь прекрасна!"
    ],
    [
        "5KmvmLb7HpI",
        "Секрет получения и приумножения гениальных знаний и мыслей. Круговорот энергии"
    ],
    [
        "XGHWKg_PIeU",
        "Directing attention to the present moment is the key to happiness. Higher Psychology"
    ],
    [
        "0pPnv3dtlHE",
        "Building a Relationship with Your Dream Is the Key to Realizing It. Higher Psychology"
    ],
    [
        "8Ko4C3kvSXI",
        "Всем плевать на тебя, для людей ты просто пыль. Пока это не поймешь, то денег не заработаешь"
    ],
    [
        "AJHQqpTUpg8",
        "Доверять Вселенной- это ВЫСШИЙ КАЙФ! Ни за что не цепляйся, отпускай и живи легко"
    ],
    [
        "e_oBU42fORo",
        "Мечта реализуется легко. Просто нужно понимать один момент…"
    ],
    [
        "ju1hcjCRKJc",
        "Этот принцип спас меня от суицида и принёс кучу бабла"
    ],
    [
        "GhTmBR0l3XA",
        "I'm stretching my skull to become more beautiful. DANGER! DO NOT REPEAT!"
    ],
    [
        "t9IKw7jNmjw",
        "ДЕВУШКА ДОЛЖНА ДОБИВАТЬСЯ МУЖЧИНУ"
    ],
    [
        "Sifj4vtHzYc",
        "Всё происходит не с тобой, а ДЛЯ ТЕБЯ. Жизнь ведёт лучшим путём"
    ],
    [
        "JoDEBCuGTsA",
        "Energy turns into MONEY. The simplest guide to wealth."
    ],
    [
        "1aryO6dqfao",
        "BLACKPILL SOLVES ALL YOUR RELATIONSHIP PROBLEMS WITH GIRLS. APPEARANCE ALWAYS MAKES THE DIFFERENCE."
    ],
    [
        "dlkQpkaCluo",
        "Женщина ДОЛЖНА платить за мужчину"
    ],
    [
        "z_QY-U6Xd8o",
        "После этого осознания жизнь начала меняться…"
    ],
    [
        "H017dnUoIPE",
        "ОЩУТИ ЭМОЦИЮ БОГАТСТВА И ЖИЗНЬ ПОМЕНЯЕТСЯ"
    ],
    [
        "d7nJd2w6SBI",
        "Девушка считает тебя лохом? Решение есть! Просто ты не делаешь это…"
    ],
    [
        "CRLmYhzVWvs",
        "Великая мудрость из Америки! Эта фраза меняет жизнь! Квантовый переход"
    ],
    [
        "Jm1dm1nzq8k",
        "Желания не материализуются?? Решение есть! Всё очень просто и сложно одновременно"
    ],
    [
        "olfFNJRF7as",
        "You were taught that life should be hard. You were FUCKED."
    ],
    [
        "UZqZWXNvN9U",
        "В этом душевном состоянии можно реализовать всё что захочешь!"
    ],
    [
        "NWhniqyanpE",
        "Сила мысли управляет твоей жизнью. Я понял великую истину. Кто чего боится- то с ним и случится"
    ],
    [
        "-XqxCUJm-9o",
        "Мир настолько конкурентный, что вы даже не представляете.  Бизнес это не для всех"
    ],
    [
        "AxwqmGVUdYQ",
        "Важность психического состояния при знакомстве с девушками. Высшая психология и пикап"
    ],
    [
        "xfkbaJfurLQ",
        "НЕ ЧИТАЕШЬ БАЗУ? СТАНЕШЬ БОМЖОМ! ЖЕСТОКАЯ ПРАВДА!"
    ],
    [
        "L9GSF5QINWQ",
        "Закон Десятины и личностная сила. Как богатство притягивается к сильным людям"
    ],
    [
        "JOXfkQsKP9Y",
        "Залип на девушку? Тебе КОНЕЦ! Но решение есть…"
    ],
    [
        "N-bCrhpRDRM",
        "Заблудился по жизни? Единственное решение проблемы"
    ],
    [
        "Z0bKbqoy0GU",
        "Личностная сила распределяет роли в социуме. Социальные игры и ранги"
    ],
    [
        "RTvOESX2fcs",
        "Радость от мечты угасает с возрастом. Важное послание. Спешите исполнить мечты прямо сейчас"
    ],
    [
        "nbIKEFsmv4o",
        "Бросила девушка? Тебе нужен BLACKPILL! Что такое черная таблетка? #LOOKSMAXING"
    ],
    [
        "Fe_YTaqOoyI",
        "The Right Tactics for Interacting with Girls. Relationship Psychology"
    ],
    [
        "Y4p32E7V_ec",
        "Личностная сила притягивает деньги и любовь как магнит"
    ],
    [
        "6A7e0u36KjA",
        "Лярвы и аскетизм. Большая опасность быть атакованным"
    ],
    [
        "Gj69Ua7aJVU",
        "Я всегда боялся стареть, но это мышление неудачника!"
    ],
    [
        "NwWsAdIoxPs",
        "Вселенная хочет тебе добра. Но есть один нюанс…"
    ],
    [
        "OZmrYXo6VBU",
        "Money isn't earned, it's attracted. How money works in our world. Lecture"
    ],
    [
        "7HAzIdhZnnk",
        "Моя главная ошибка в бизнесе на ютубе"
    ],
    [
        "PV_51ayUjhM",
        "Самая глупая трата энергии"
    ],
    [
        "NmfmiaZ7N-o",
        "Жалость к себе портила мне жизнь постоянно. Решил всё поменять"
    ],
    [
        "YfPa0jb6qbs",
        "Единственная причина отказа при знакомстве. Хватит себя обманывать"
    ],
    [
        "DymIhoYA7fc",
        "Закон Десятины работает ВСЕГДА  и делает меня БОГАЧЕ каждый день"
    ],
    [
        "tnCkOfgkIis",
        "Self-Confidence from a Psychological Perspective. Why Are You Insecure? The Answer is Simple"
    ],
    [
        "EHKEJ1PhGHg",
        "Чувство вины перед окружающими уничтожает твою жизнь"
    ],
    [
        "qgjDHqK2otI",
        "Зависть всегда приводит к нищете"
    ],
    [
        "XnNGpyflIEg",
        "В тебе уничтожили главное качество для успеха(очень редкое качество)"
    ],
    [
        "31H4J9QMEak",
        "Personal Power Is a Magnet for Women (And Money)"
    ],
    [
        "QxoMw698HGM",
        "Единственный способ подняться по жизни. Только так побеждают"
    ],
    [
        "4mpmfD0rsG8",
        "Отношение к отцу определяет твой успех. Высшая психология"
    ],
    [
        "soMLGhn6iJ0",
        "Почему не везет в отношениях? Причина одна"
    ],
    [
        "OkZAPTWf-AE",
        "Осуждая других- закапываешь себя. Тварь ли я дрожащая или право имею?"
    ],
    [
        "XDRuZv3Qf0Y",
        "All fears are the devil. In God there is no fear."
    ],
    [
        "zhB7DeI1jPw",
        "The only way to get a girl to like you. I've tested it myself."
    ],
    [
        "p0QDlg_wr7Q",
        "Transformed my look from UGLY to MODEL"
    ],
    [
        "7rOsGDIWm1Y",
        "Стал богатеть с помощью силы мысли"
    ],
    [
        "4usyoIdJsig",
        "лекарство от п*здострадания"
    ],
    [
        "HcVO-t89PXc",
        "The Devil Controls Through Pleasure"
    ],
    [
        "YbN4m16fgN4",
        "Я собирался умирать, но Бог спасал меня всегда"
    ],
    [
        "qP7JG_gV_ew",
        "Вселенная всегда даёт подсказки и никогда не оставляет"
    ],
    [
        "vRNNMNeB2cc",
        "Как я взломал эту жизнь. Главный вселенский закон"
    ],
    [
        "9ylLyrMmb-k",
        "Бросил курить с помощью СИЛЫ МЫСЛИ. Простейший взлом психики"
    ],
    [
        "ghp63BJJwfs",
        "Hard work leads to poverty. Big money is earned without effort."
    ],
    [
        "Vu_cOR3E-g0",
        "Твои вибрации создают жизнь мечты. Очень легко!"
    ],
    [
        "25qYwNBibRo",
        "Управлять реальностью легко! Нужно всего лишь сделать это.."
    ],
    [
        "gAT8xRqbbec",
        "Transforming pain into infinite power. This practice isn't for everyone. The pain egregor."
    ],
    [
        "i9q36czQKsA",
        "How I fight evil spirits and get out of trouble"
    ],
    [
        "kBqoBmm3-rk",
        "Личностная сила это чит-код для твоей жизни"
    ],
    [
        "1AD_mRSdM9w",
        "притяжение людей в свою жизнь силой мысли"
    ],
    [
        "5JUDS4cmDAA",
        "Починить свою судьбу? легко!!!"
    ],
    [
        "qhe1H_R_Rig",
        "Что делать с психотравмами? Простейшее решение которое изменит жизнь"
    ],
    [
        "UPlTDUKfI6A",
        "The world exists only for you"
    ],
    [
        "YCHUud8c3PM",
        "дьявол обманул вас всех"
    ],
    [
        "0_gJL_YbreY",
        "Синдром самозванца ломает тебе жизнь"
    ],
    [
        "IxTf9MTqtrU",
        "Синдром самозванца приводит к нищете"
    ],
    [
        "5miVcpGlVBk",
        "Swearing Drains Your Energy"
    ],
    [
        "MSgqh8ej-2w",
        "The easiest way out of POVERTY! It couldn't be simpler."
    ],
    [
        "g_fM5440-GI",
        "Блокировка сексуальности человека через психотравмы"
    ],
    [
        "XiioZdygxTw",
        "Святой дух в жизни человека"
    ],
    [
        "PWh2avf0Uzk",
        "Большинство людей мазохисты! Они хотят страдать!"
    ],
    [
        "-y8wNLmfY_g",
        "The Cure for Social Anxiety"
    ],
    [
        "iVGmFaiE-A4",
        "Святой дух и состояние потока. Бог есть любовь"
    ],
    [
        "4Ssr0NLg4p0",
        "Главный секрет привлекательности"
    ],
    [
        "UZUAzKdDdVk",
        "Бог это ИЗОБИЛИЕ"
    ],
    [
        "I9wRpapypvQ",
        "Визуализируй жизнь мечты!"
    ],
    [
        "BbtVTJ56jbw",
        "God gave me a sign and I almost cried with happiness."
    ],
    [
        "G1W2T6Nixmc",
        "Я НЕ ХОЧУ СДОХНУТЬ НА ЗАВОДЕ!!! БОГ НАКАЖЕТ ЗА ЭТО?"
    ],
    [
        "9BrOxWQVQfU",
        "Плохие мысли разрушат твою жизнь"
    ],
    [
        "aTThfzsKEds",
        "The universe despises such people."
    ],
    [
        "4o5HOnOVUto",
        "Простая инструкция к богатству"
    ],
    [
        "AdfLxoqyDiA",
        "Я отвернулся от нищих знакомых. Рабские программы подсознания и отсутствие веры"
    ],
    [
        "gKuEf8ji_A0",
        "Вселенная проверяет нас каждый день. Ты должен пройти проверку"
    ],
    [
        "iuPkkbaa7k0",
        "Я беру от жизни ВСЁ что захочу! Подсознание формирует реальность"
    ],
    [
        "CulaoheXpY0",
        "Деньги делать легко! Просто убери стеснительность!"
    ],
    [
        "SndXI4uMBrI",
        "Единственный способ ПОДНЯТЬСЯ! Я переехал в Голливуд"
    ],
    [
        "2PfwD3Tx0D0",
        "I make money out of thin air. Energy transformation and sublimation."
    ],
    [
        "ewVMUpzRibI",
        "Тревожность, депрессия, апатия? Это видео СПАСЁТ ТЕБЯ!"
    ],
    [
        "gC-8UdPcq-Q",
        "Жизнь большинства похожа на мучение"
    ],
    [
        "5FJqW81WBfk",
        "The kid doesn't give a damn and lives life to the fullest! A deputy's son!!"
    ],
    [
        "oouik1PlZbQ",
        "Расслабься и живи по кайфу! Удача любит тех кому плевать на всё"
    ],
    [
        "P-QPUUpOuEs",
        "Как я развиваю ютуб. Деньги с воздуха"
    ],
    [
        "7igD4wnqA6w",
        "Всегда плати добром на добро и будет тебе счастье"
    ],
    [
        "REVjpZcj2ts",
        "Тебя в школе приучили оправдываться. Это признак РАБА"
    ],
    [
        "75E0Yux4TQM",
        "Почему ты до сих пор никто? Рабские прошивки подсознания"
    ],
    [
        "5RE-GXQN9Lo",
        "Я социофоб. Я боюсь женщин и не уважаю себя. Что делать?"
    ],
    [
        "DymMviat2zI",
        "Почему ты до сих пор не заработал денег ? Не хватает ответственности"
    ],
    [
        "PNzUk1UAPCs",
        "Я боюсь женщин. Я низкоранговый. Что делать?"
    ],
    [
        "TQYmwiGE5Ck",
        "почему женщины не дают даже если ты идеальной внешности"
    ],
    [
        "J3D88OZKNlw",
        "Отпусти негатив из прошлого и вдохни новую ЖИЗНЬ"
    ],
    [
        "virUDnAtpA0",
        "Нестабильность психики видна сразу #психология"
    ],
    [
        "ZWXkG_b_5qQ",
        "Ложная социализация это проблема большинства людей #психология"
    ],
    [
        "4icAZnjXMtg",
        "состояние жертвы"
    ],
    [
        "Q646tJ3BgSw",
        "Вся Вселенная существует ТОЛЬКО для тебя"
    ],
    [
        "BJNHzjjH9kk",
        "Thoughts materialize very quickly. The main secret"
    ],
    [
        "bl6LVsqaqJE",
        "My Louis Vuitton wallet brings me FREE money. Subconscious and viruses"
    ],
    [
        "nuw-odbskM0",
        "I UNDERSTOOD THE UNIVERSAL LAWS AND OBTAINED A US VISA BY THE POWER OF THOUGHT"
    ],
    [
        "odQREO4XgTM",
        "Your psyche was broken as a child. This will lead to a tragic end..."
    ],
    [
        "HscdSTZDJHU",
        "мы запрограммированы на тревожность"
    ],
    [
        "_T-m64kBaew",
        "Почему тебе не дают девушки? Профессор отвечает"
    ],
    [
        "D1pJrFyBhQ0",
        "Girls only like THIS kind! Pick-up artists lied to you."
    ],
    [
        "1PSwLqTqmHc",
        "я терпеть не могу нищету!!! совковые прошивки и любители халявы"
    ],
    [
        "1c59qsqzRcg",
        "Beating the Poverty Mindset Out of Your Brain"
    ],
    [
        "U2gKoOgnpaQ",
        "HOW I LEFT THE MATRIX AND OVERCOME POVERTY"
    ],
    [
        "0cky2YKJRHc",
        "ОСНОВЫ МУЖСКОЙ ПРИВЛЕКАТЕЛЬНОСТИ! ЖЕНЩИНЫ ХОТЯТ ДВЕ ВЕЩИ"
    ],
    [
        "M-oquFDRDhU",
        "почему девушки не дают? высшая психология"
    ],
    [
        "LHoeDW9r4Q8",
        "ПЕРВАЯ НЕДЕЛЯ ВЕГАНСТВА 🥑 КАКОЕ ГЛАВНОЕ ИЗМЕНЕНИЕ?"
    ],
    [
        "LgTElg38grg",
        "СОЛНЦЕ это вред или польза? Моё мнение- для одних польза 🌅 для других смерть ☠️"
    ],
    [
        "XJqYALTlcds",
        "Accepting death is the BEST CURE for anxiety. Inner peace as a goal in life"
    ],
    [
        "AQv10EaBUiQ",
        "Сатанизм на открытии олимпиады в Париже. И почему это хороший знак 👍"
    ],
    [
        "txSwapj_nUA",
        "Травматизация психики как точка БЕЗГРАНИЧНОГО РОСТА. Высшая психология"
    ],
    [
        "KXWo_BOI_wA",
        "Тебе ВНУШИЛИ что деньги зарабатываются тяжело. Тебя НА*БАЛИ. Прошивка на нищету"
    ],
    [
        "KJs-0zgc_wE",
        "Уровень жизни зависит от твоих ВИБРАЦИЙ. Половое воздержание"
    ],
    [
        "mkGqGMDV0-g",
        "HEALING ONESELF THROUGH EGO DESTRUCTION"
    ],
    [
        "9G6qsva_xoE",
        "Тебя бросила баба?? ЛЕКАРСТВО ЕСТЬ!"
    ],
    [
        "rUS7mmS8xIM",
        "ХВАТИТ УНИЖАТЬСЯ ПЕРЕД ДЕВУШКОЙ"
    ],
    [
        "FpE8gxUp97M",
        "ЭТО СДЕЛАЕТ ИЗ ТЕБЯ СВЕРХЧЕЛОВЕКА! ТЕРПЕНИЕ И ТЕРПИЛЬСТВО- В ЧЕМ РАЗНИЦА?"
    ],
    [
        "8F0r9ykQ20c",
        "Бывает два вида с*екса. Один тебя уничтожит. Второй тебя наполнит и поднимет."
    ],
    [
        "5SBMpH2e7zI",
        "ЛУЧШИЙ СПОСОБ ВЛЮБИТЬ ДЕВУШКУ"
    ],
    [
        "xxeqwyNRe-0",
        "An original method to get a girl to like you"
    ],
    [
        "VTA12jkuZjQ",
        "WHO ARE YOU, YOU BEAST? THE MAIN SECRET OF ABSTINENCE"
    ],
    [
        "UK9bf81IWm8",
        "ЖЕСТКО ПОЕХАЛА КРЫША. ИДУ КРИЧАТЬ В ЛЕС. СОСЕДИ ВЫЗВАЛИ ДУРКУ"
    ],
    [
        "ejjiRFG0OaI",
        "травмированные женщины СЛОМАЮТ тебе жизнь(видео ни о чем)"
    ],
    [
        "SgVM68SyPNQ",
        "ты должен быть особенным. секрет жизненных достижений"
    ],
    [
        "BjJR_rGE_YY",
        "лучшее видео про воздержание"
    ],
    [
        "Vo-cKP3oQng",
        "Альфа самец и сигма. В чем отличие?"
    ],
    [
        "FlJ0chdASiw",
        "Самый ВЫСШИЙ ранг среди мужчин"
    ],
    [
        "f8Xxu1082sk",
        "когда тебе пришел конец"
    ],
    [
        "YBOnpp42jXg",
        "Иисус с точки зрения психоанализа"
    ],
    [
        "XSV91DWw3dw",
        "ВОССТАНОВЛЕНИЕ ПСИХИКИ САМОСТОЯТЕЛЬНО"
    ],
    [
        "ApEL-W40aVg",
        "A LIFE HACK TO MAKE A GIRL FALL IN LOVE"
    ],
    [
        "CRMrpGR_crU",
        "ПОСТТРАВМАТИЧЕСКОЕ РАССТРОЙСТВО И ПСИХОДЕЛИКИ"
    ],
    [
        "D4Uxnfx2HsU",
        "THE SCARY TRUTH ABOUT RELATIONSHIPS 💔"
    ],
    [
        "Z4IOs9FY-gk",
        "У МУЖЧИНЫ НЕТ ШАНСОВ В ОТНОШЕНИЯХ!"
    ],
    [
        "Vrjco2ROqfk",
        "ЛУЧШИЙ СПОСОБ ПОДНЯТЬ СВОЙ РАНГ И ТЕСТОСТЕРОН"
    ],
    [
        "ATJpkPimAEE",
        "Spend your time productively"
    ],
    [
        "U3KoV3l9KGo",
        "ГЛАВНОЕ ОТЛИЧИЕ БЫДЛА ОТ ЧЕЛОВЕКА"
    ],
    [
        "s6p0kqe5GYk",
        "Арсен Маркарян"
    ],
    [
        "X-cl2WdkV68",
        "ФУТБОЛ НАУЧИЛ МЕНЯ…"
    ],
    [
        "zD9F-Ui6n-o",
        "ФРАНЦИЯ ПРЕВРАТИЛАСЬ В АД! ГОСПОДИ СПАСИ НАС!"
    ],
    [
        "BkJDDWjSnzo",
        "ВСЯ ПРАВДА ПРО ВОЗВРАТ БЫВШЕЙ!ОЧНИТЕСЬ"
    ],
    [
        "-BctgQOhvtQ",
        "TWO FUNDAMENTAL TYPES OF NUTRITION"
    ],
    [
        "Rzrir79wtvw",
        "THE WHOLE TRUTH ABOUT RELATIONSHIPS"
    ],
    [
        "4ik7b6WXEQg",
        "НОВАЯ ЖЕНСКАЯ МАНИПУЛЯЦИЯ!!! Смотреть всем!"
    ],
    [
        "78BahfjI_2c",
        "Не предавай себя! Топовая мужская БАЗА"
    ],
    [
        "GfhAFUNzB9s",
        "Male and Female Perceptions of the World. The BEST lecture on psychology."
    ],
    [
        "7rcTI6wyssU",
        "Как я зарабатываю на ютубе? (Секрет любого бизнеса)"
    ],
    [
        "SbpHWta9b1Q",
        "почему я ещё не повесился?"
    ],
    [
        "V_eixNEFJ_M",
        "курение убивает в тебе мужчину"
    ],
    [
        "0POXve3P-Wk",
        "книга для тех кто живет по понятиям"
    ],
    [
        "9Oz1zWG1yhI",
        "the strangest and creepiest philosophical book"
    ],
    [
        "pFD13Y9KU54",
        "Голодание очищает душу"
    ],
    [
        "n67dDefzRT0",
        "ЛУЧШАЯ КНИГА ДЛЯ МУЖЧИН"
    ],
    [
        "TK9njIkJ3Dg",
        "Как я выучил три языка"
    ],
    [
        "-_5CmXUMc4s",
        "Masturbation ruined my life."
    ],
    [
        "SX1C-58tHrA",
        "женщину добиться НЕВОЗМОЖНО. я вам докажу"
    ],
    [
        "he0jFoBubPo",
        "I WAS A TOTAL FLORAL LOSER. Don't repeat my mistakes"
    ],
    [
        "32OUo5J-B0A",
        "женщина тебя БРОСИТ когда начнутся проблемы"
    ],
    [
        "umpzjWeB8xo",
        "kill the POVERTY in yourself"
    ],
    [
        "aHFfyxn_sHs",
        "Мир это тюрьма. ГЕНОЦИД людей со стороны власти"
    ],
    [
        "l6Ss_7EIeIA",
        "важнейший совет для ДЕВСТВЕННИКОВ"
    ],
    [
        "ZVrxM6eSF2U",
        "как ВЫСШИЕ СИЛЫ спасли мой телеграм канал"
    ],
    [
        "bT05KLv5qjE",
        "вся суть МАСТУРБАЦИИ. Половое воздержание намного сложнее чем кажется"
    ],
    [
        "ZEnNvFl0Xws",
        "99% of women are UNFIT for marriage"
    ],
    [
        "Q8pBcSjp2Eg",
        "How I got a BLACK DIPLOMA"
    ],
    [
        "DjCSCZORXjk",
        "cortisol fixation and mental trauma"
    ],
    [
        "o4jC24qNleg",
        "I only grasped these fundamentals at 25…"
    ],
    [
        "ZwueWQP1hII",
        "мужчина обязан чувствовать БОЛЬ ради своего развития"
    ],
    [
        "HnpYwujXnQk",
        "главная ПРОБЛЕМА мужского движения"
    ],
    [
        "4VRGwbnPjsE",
        "Главный секрет достижений в жизни"
    ],
    [
        "014au_LgwGA",
        "Каждый имеет право на ошибку"
    ],
    [
        "lHApzmFj2GU",
        "Быдло и падаль всегда будут жить ПЛОХО"
    ],
    [
        "SRrILqYoShE",
        "Утро прозревшего мужчины. Топим в 5 утра VLOG"
    ],
    [
        "dMP1h-LPJaQ",
        "I was cured of ALENISM thanks to one blogger. Men's movement"
    ],
    [
        "F8okUuqHz7o",
        "The Best Cure for Demons and Devils: An Exorcism Guide"
    ],
    [
        "FtULef_DpXI",
        "самый ХУДШИЙ спортпит! Чуть не умер"
    ],
    [
        "xIA-UWcMgQY",
        "Я был одержим бесами. Исповедь живодёра"
    ],
    [
        "rtcvAfYSocY",
        "My Journey from a Monster to a Human"
    ],
    [
        "VB5rD2PHMbI",
        "Как работает карма? Простейшее объяснение"
    ],
    [
        "NTerL903frU",
        "Alenism Ruined My Life. Confessions of a Scavenger"
    ],
    [
        "8u1bXI2einQ",
        "Сними разорванный пельмень с головы"
    ],
    [
        "Mgvzlf19knU",
        "Не искушай Господа своего. Моё трактование этой фразы"
    ],
    [
        "gW9Wx447XsM",
        "Страха нет. Моя философия. Каждый ответит за слова"
    ],
    [
        "2fhJFDDanxA",
        "Human vibrations influence intelligence"
    ],
    [
        "XDL-uKoMlss",
        "Развод на бабки на сайтах знакомств"
    ],
    [
        "MRr9W9_Gw4s",
        "КАСТРАЦИЯ мужчин в современном обществе"
    ],
    [
        "01JZ5ktQA0s",
        "Бог избавляет от зависимостей. Половое воздержание"
    ],
    [
        "25tVchMMers",
        "Я живу без страха и умру без страха"
    ],
    [
        "sMwJ3WaTVQU",
        "Страх знакомиться с девушками. Причины и лечение"
    ],
    [
        "f8FQMCMCQwM",
        "The Best Tactic for Abstinence. Abstinence and Life Success"
    ],
    [
        "btqm-sRevTE",
        "девушки дают ТОЛЬКО таким парням"
    ],
    [
        "r_E6aF10Pqo",
        "ты (не) обязан быть слабым"
    ],
    [
        "f3cegcpTdoU",
        "Лечение порнозависимости. Секрет воздержания. Оргазм и кортизол"
    ],
    [
        "Qm_Rx6bSaKc",
        "The Magic of Abstinence: Living with Joy and Healing the Mind"
    ],
    [
        "a7uO3QXQesA",
        "Борьба с демонами. Порнография, наркозависимость, уныние"
    ],
    [
        "s9Ta5sZRM0M",
        "Когда жизнь рушится на глазах"
    ],
    [
        "_6JfgnszOs0",
        "Десексуализация мозга. Порнозависимость, аленизм и неокортекс"
    ],
    [
        "x8hiesHVCUY",
        "Что такое ЭГО и почему это ПЛОХО? Основы психоанализа"
    ],
    [
        "-6XnhtNQKu0",
        "Страдание всегда идёт на пользу. Страдание исцеляет. Моя философия"
    ],
    [
        "TP1EWJYEbCY",
        "Dopamine System Issues: How to Identify and Treat Them? Mental Health Struggles Due to Masturbation"
    ],
    [
        "UfZfJgnvGOk",
        "Why Does God Send Trials? The Easiest Way to Overcome Any Challenge"
    ],
    [
        "nna4J5yF29I",
        "Как и зачем Бог даёт испытания? Шокирующая правда"
    ],
    [
        "A49aAb2wOPE",
        "Why is the right path so difficult? Abstinence and asceticism. Strength of spirit."
    ],
    [
        "nisSfMoUhOI",
        "The secret to happiness and the meaning of life. Few will understand."
    ],
    [
        "bkMYNZcv9cM",
        "горькая ПРАВДА про отношения с девушками"
    ],
    [
        "aTuwHavDK_M",
        "Цифровой аутизм. Лечение и профилактика"
    ],
    [
        "8H3jxQ94DUY",
        "The Practice of Silence. Neuroresource. Why is silence beneficial?"
    ],
    [
        "9bEI-YK1bCU",
        "Социальных лифтов не существует"
    ],
    [
        "ZPs5TklM1nM",
        "The cause of all phobias and fears. How did I cure all my phobias?"
    ],
    [
        "h6aU_ywXAek",
        "Важнейший навык для всех мужчин. Психология отношений"
    ],
    [
        "6jFF_oE38dc",
        "You don't need a woman"
    ],
    [
        "X0U842nW5Z8",
        "What do women want most?"
    ],
    [
        "8te2h5gX-2E",
        "Feminine parenting LOWERS your testosterone"
    ],
    [
        "sp-Ul2IY6B8",
        "Girls don't care about you and your life."
    ],
    [
        "HogQzNlsuFA",
        "Невозможно добиться успеха если этого не знать"
    ],
    [
        "X_FHCa-8CgY",
        "The most terrible sin. A direct road to hell is guaranteed."
    ],
    [
        "gymXIG4w4cY",
        "Социофобия. Болезнь 21-го века"
    ],
    [
        "KB3d4GwRvKY",
        "Боязнь девушек. Как я боролся со страхом и неуверенностью"
    ],
    [
        "GqHGkV0oS4w",
        "Лучшее новогоднее поздравление для мужчин. Мужская база и развитие"
    ],
    [
        "9anOrMsk39k",
        "Альфа самец и омега. Главное отличие. Вы этого не знали"
    ],
    [
        "MLkNrabBzhI",
        "Поколение поломанных мужчин. Мой способ как стать мужчиной будучи тряпкой"
    ],
    [
        "dqarebUUHSw",
        "Жестко качаюсь во имя Иисуса Христа"
    ],
    [
        "ALwdJqbmrpQ",
        "You are a diamond in the rough. Clean off the dirt"
    ],
    [
        "OgfuGBapGjs",
        "Why does nobody love you?"
    ],
    [
        "NxR-9QGrOnE",
        "Girls feel your insides right through and through"
    ],
    [
        "2_QfvxpC_XU",
        "ЕДИНСТВЕННАЯ причина срывов на воздержании! Бросить онанизм за пять минут реально"
    ],
    [
        "vzCFX_uEzqk",
        "Высшая психология отношений. Это должен знать КАЖДЫЙ (Почему твоя девушка уйдет от тебя)"
    ],
    [
        "mDIIB-bkouU",
        "Борьба с собственными демонами. Мой опыт"
    ],
    [
        "BPF4uavCkSg",
        "Высшая психология отношений за 14 минут"
    ],
    [
        "2lL1795keLg",
        "Reality Transurfing: My Experience of Manifesting Desires"
    ],
    [
        "wKphza28sfU",
        "почему девушки перестали ЛЮБИТЬ"
    ],
    [
        "f-ugMq286KI",
        "воздержание сделает из тебя СВЕРХЧЕЛОВЕКА"
    ],
    [
        "SrwT175NddQ",
        "Весь смысл воздержания за 6 минут"
    ],
    [
        "VNnCdN4NdPQ",
        "Воздержание и привлекательность. Девушка раскрывает СЕКРЕТ"
    ],
    [
        "2Epy2dGsciY",
        "overcome porn addiction"
    ],
    [
        "MJQGDXXQ1DQ",
        "как бросить порнозависимость и остальные зависимости"
    ],
    [
        "aw2E8_o3kqM",
        "My way to get pumped up without drugs"
    ],
    [
        "ft9KPDMi0P4",
        "как не опозориться? это должен знать каждый"
    ],
    [
        "ypd3G_0M-8M",
        "saved my life.."
    ],
    [
        "_nCUrx2yVLg",
        "my review…"
    ],
    [
        "lRvkTjml_o8",
        "Жизнь поменялась после ЭТОГО… Секрет исполнения желаний"
    ],
    [
        "rR-kTh7uSS8",
        "ДЕВУШКИ СХОДЯТ С УМА от этого аромата…"
    ],
    [
        "SC4nJphxFaU",
        "навсегда…"
    ],
    [
        "GpGZSEz2Frk",
        "Thoughts are things. Negative thoughts kill and turn your life into hell."
    ],
    [
        "pMBlbVgCWZY",
        "The world is a mirror. What you think about is what you get."
    ],
    [
        "NkyhbSfh6O0",
        "СЕКРЕТ излечения от ВСЕХ вредных привычек. Самый рабочий способ"
    ],
    [
        "0_nHtilpeUo",
        "Лучший повседневный аромат? Новинка 2023 YSL MYSLF"
    ],
    [
        "Y_XAgYRPxhc",
        "Abstinence and Attractiveness: Why Girls Don't Look at You"
    ],
    [
        "nt5joirXswg",
        "Секрет удачи и благосостояния. Читкоды в реальной жизни"
    ],
    [
        "bI7Eku9GTsk",
        "Abstinence and attractiveness. The main secret…"
    ],
    [
        "rE41mt85eyA",
        "Причина срывов на воздержании. А так же секрет привлекательности"
    ],
    [
        "RpQz51B9unE",
        "How ALL men on Earth were screwed over"
    ],
    [
        "3i8Zj-ZzpF8",
        "Что я понял за полтора года отшельничества… Жизнь никогда не будет прежней"
    ],
    [
        "8rObxG-sc_Q",
        "Твоя мать сломала тебе психику. Поколение слабых мужчин. Омежки и опущи"
    ],
    [
        "2KEQG1Jw8FU",
        "Я разгадал секрет удачи. Как управлять удачей? Магическая сила добрых поступков"
    ],
    [
        "yg9t5_8GCX4",
        "Самая страшная болезнь 21 века. Социальное программирование"
    ],
    [
        "F1jAaDb3Uyw",
        "Как управлять удачей. Как подчинить себе удачу и использовать её в своих целях"
    ],
    [
        "bDIRIVF-JtU",
        "Вселенский закон десятины помог мне выбраться из нищеты. Пожертвования всегда возвращаются"
    ],
    [
        "aj5_AHYCgpY",
        "The Magical Power of Abstinence. Fulfilling Desires During Sexual Abstinence"
    ],
    [
        "3fzVLZJPLuw",
        "Spent my last money on perfume. Nothing left for food. Still haven't saved up for my own funeral"
    ],
    [
        "w94JXrpJOYw",
        "Judge not, and ye shall not be judged. The most important law of our life."
    ],
    [
        "W554ptI9oYA",
        "The universal law of tithing always works. Monetary donations attract good fortune."
    ],
    [
        "5npEEhmtNJI",
        "Вселенский закон десятины. Как пожертвования влияют на твою удачу"
    ],
    [
        "ShUHHaIRcGQ",
        "Вселенский закон десятины. Почему важна благотворительность"
    ],
    [
        "YMoOUEp2Dfw",
        "Brainwashing through movies and TV series. Alenism. The egregor of the torn donut"
    ],
    [
        "RbcKVrk77vE",
        "Heaven and Hell. The Feeling of Abandonment. Religious Egregor"
    ],
    [
        "-ygXCHPhYU4",
        "Твоя девушка не хочет чтобы ты развивался и становился лучше"
    ],
    [
        "Cr8y3JcZZBk",
        "Божественное чудо произошло со мной. Святое Евангелие против дьявола"
    ],
    [
        "WLuKRWsJHTw",
        "Трудный выбор в жизни? Решение есть! Секреты философов"
    ],
    [
        "FWs4GdAdqJU",
        "How I Hacked Our Matrix. A Crazy Story. A Cheat Code for Real-Life Money"
    ],
    [
        "hCLCqdwcDgk",
        "The Divine Principle in Every Person. My Philosophical Reflections"
    ],
    [
        "wJiVAWq01Lg",
        "ИЗБАВЬСЯ от всех заболеваний благодаря солнцу"
    ],
    [
        "wrL7KckWVxM",
        "Почему необходимо ходить босиком по земле. Вибрации земли и статическое электричество в мозге"
    ],
    [
        "PKXyDPGm-v8",
        "Моя борьба со стрессом и страхами. Кортизол и понимание вселенских законов"
    ],
    [
        "0NRk8-GlkUE",
        "Stress Kills. And How to Cure Any Disease Without Medication"
    ],
    [
        "yd25Brymzf0",
        "причина всех вредных привычек"
    ],
    [
        "b3aNqQb1QpI",
        "Adrenal fatigue and stress. Cortisol and quality of life."
    ],
    [
        "5Bf0bDpnnYw",
        "NEVER perform cunnilingus! A psychologist's opinion"
    ],
    [
        "1k1yQTD2OfI",
        "Эффект плацебо. Сила самовнушения. Как мысли влияют на наше здоровье"
    ],
    [
        "f_IqFslCz1Y",
        "Поллюции и как с ними бороться. Половое воздержание"
    ],
    [
        "StTmJ-HRTpY",
        "Биополе человека. Вибрации человека и энергетика"
    ],
    [
        "CPaYBLOzZBQ",
        "The influence of thoughts on a person's life. The power of thought. Where to invest money."
    ],
    [
        "uYTLPfVRl9s",
        "Почему девушки разучились любить"
    ],
    [
        "WCTNTG708Rw",
        "Как выглядит психологическая смерть?"
    ],
    [
        "y8wiAmT7MUg",
        "Как я пережил психологическую смерть"
    ],
    [
        "vrM-WJ-k250",
        "Why should we rest on Saturday? Universal energy and success in life. The main rule of the Jews"
    ],
    [
        "iB27NYKA-V0",
        "Стоицизм и благодарение. Мощнейшие практики. Становись счастливым уже сегодня"
    ],
    [
        "fkJ7ScN7Uq8",
        "Почему ты убиваешь своё время ? Воздержание и ценность времени. Дофамин и энергия"
    ],
    [
        "_LZ33q6_T5k",
        "забудь про стресс НАВСЕГДА. Самый эффективный способ борьбы со стрессом"
    ],
    [
        "Ucl_BRx2jzQ",
        "Важнейшая еврейская МУДРОСТЬ! подходит для всех!"
    ],
    [
        "6tgmas41FBk",
        "Почему женщины перестали любить мужчин. Мнение психолога"
    ],
    [
        "XCCdFMmfJ5g",
        "Depression during abstinence. Who's to blame?"
    ],
    [
        "hv5xqj59V1M",
        "как преодолеть тяжелые моменты жизни"
    ],
    [
        "t3dgHTxKAjs",
        "What I realized in a year and a half of solitude"
    ],
    [
        "18L2JvHgAAY",
        "эта привычка ИЗМЕНИТ твою жизнь. Выход из дофаминовой ямы и достижение целей"
    ],
    [
        "koGEygvg5pA",
        "девушки не любят СЛАБЫХ мужчин. Половое воздержание и привлекательность. Мужская сила"
    ],
    [
        "wy8DZPCt6yc",
        "Abstinence and Attractiveness. Girls Only Want Men Who Practice Abstinence"
    ],
    [
        "j6DBopgmvm0",
        "Почему твоя  женщина ВСЕГДА в активном поиске ?"
    ],
    [
        "3rWSlIK9khg",
        "How does abstinence affect your appearance?"
    ],
    [
        "59g64GrLQsI",
        "Abstinence and SUCCESS in Life. Dopamine and Motivation"
    ],
    [
        "0IuoYH_6Apk",
        "Watch this video if you're LONELY. Dopamine and loneliness. Abstinence and the thrill of life. As..."
    ],
    [
        "F2-GJa5G_hg",
        "Причина срывов на воздержании. Ты больше не будешь срываться после этого видео"
    ],
    [
        "OP6CkLsdSDU",
        "Воздержание и привлекательность. Невозможно притягивать женщин и деньги без воздержания"
    ],
    [
        "ZcERwMODA5E",
        "Abstinence affects luck. I was shocked by how it works. Esoterics"
    ],
    [
        "lRj__wGHTUk",
        "Два важнейших шага для счастья. Половое и информационное воздержание"
    ],
    [
        "OUhQlXfKo4Y",
        "There are only two causes of depression. There are no other causes."
    ],
    [
        "-UnPkA3cYlk",
        "WHY ABSTINENCE SOMETIMES DOESN'T HELP"
    ],
    [
        "upqtVsOp-4U",
        "КАК ПРИТЯГИВАТЬ ДЕНЬГИ В СВОЮ ЖИЗНЬ? Я ВСЁ ПОНЯЛ"
    ],
    [
        "0orELG6aeAg",
        "ALENISM AND DOPAMINE. WHAT'S THE CONNECTION? My own formula. A thesis in psychology."
    ],
    [
        "USIwZSNx_6s",
        "КАК ВЕРНУТЬ БЫВШУЮ ДЕВУШКУ? 100% способ, работает всегда"
    ],
    [
        "epH6e0alTbs",
        "ПОЗНАКОМИТЬСЯ С ЛЮБОЙ ДЕВУШКОЙ ЭТО ЛЕГКО. ЧТО ТАКОЕ РАНГ В ОТНОШЕНИЯХ?"
    ],
    [
        "E1jLWSV3yUI",
        "I became a God of aesthetics without steroids. A guide to fitness and aesthetics."
    ],
    [
        "ZQTxQwfkiPY",
        "Всем войнам посвящается. Сила духа взлетит после этого видео"
    ],
    [
        "pka0PUrg1xU",
        "Два важнейших правила чтобы стать мужчиной. Как я стал альфа-самцом? Мужское развитие"
    ],
    [
        "Esq5DX9te4s",
        "ТЫ УДАЛИШЬ ТИНДЕР после этого видео ⛔️ Вот почему ты не можешь найти девушку"
    ],
    [
        "6iIr5_2m_tI",
        "Women go crazy for these men. The main secret"
    ],
    [
        "3v-Wzkf4NjE",
        "Abstinence and the Gym 💪 Prolactin and Testosterone. You Won't Be Able to Get Shredded Without Ab..."
    ],
    [
        "yWGtwa3xbRA",
        "I took cold showers for a whole month. What changes?"
    ],
    [
        "XIH0l2bv8fo",
        "Сатана не дремлет. Дискриминация и расизм⛔️⚠️ Будьте осторожны"
    ],
    [
        "BAE-AB2C3-4",
        "Abstinence and attraction. The main trap of abstinence. I broke my abstinence without meaning to."
    ],
    [
        "cerjXAuuwDA",
        "VLOG#3 выживание во Франции"
    ],
    [
        "czaEYcBgVyU",
        "Место силы. Как получать энергию от Вселенной на халяву? Где искать места с хорошей энергетикой?"
    ],
    [
        "64-A5DQMkag",
        "Почему БЫВШАЯ НЕ ВОЗВРАЩАЕТСЯ? 👎 Не могу вернуть бывшую 😢"
    ],
    [
        "LTNWsr-SM-8",
        "Как работает карма? Объясняю принцип. Вы будете в шоке. Убил человека и оказался в аду на Земле"
    ],
    [
        "JofpfmFiGlE",
        "Становая тяга ☠️ Чуть не стал инвалидом в тренажерном зале. Не повторяй моих ошибок"
    ],
    [
        "hS_hYpzKiuM",
        "VLOG #2: Survival in France. Maximum Difficulty"
    ],
    [
        "BKYevqvLpqY",
        "VLOG#1 выживание во Франции. Дискриминация русских"
    ],
    [
        "3KVSAjQv-J8",
        "Тестостероновые бабы и пролактиновые мужики"
    ],
    [
        "GN7Ng5zPSq0",
        "Как Вселенная исполняет любые желания и спасает от смерти ? Объясняю принцип. Большой подкаст"
    ],
    [
        "7JpGVpfTvOk",
        "The best way to boost your self-confidence. Raise your rank and become the king of this life."
    ],
    [
        "tXbdyjGJKUs",
        "Выжигатель мозгов существует. Чуть не сошел с ума. Берегите свою голову !"
    ],
    [
        "KbnXIr0qUmM",
        "Как найти девственницу? Как проверить девственность?"
    ],
    [
        "x9r8o_hpONM",
        "Female Virginity. Does It Matter or Not? Psychology of Relationships"
    ],
    [
        "TYYPML0a0BI",
        "Разоблачение Максима Вердикта. Обзор на Максима Вердикта от психолога"
    ],
    [
        "jfjm3inGBYM",
        "How do they destroy masculinity? How do they degrade men? Maxim Verdict turns you into idiots."
    ],
    [
        "JD-crH-8KjQ",
        "Половое воздержание не работает. Что делать ?"
    ],
    [
        "DtNn80-luIU",
        "Abstinence and Attractiveness. It Works 100% A True Story"
    ],
    [
        "bYczLWrdfuI",
        "How I got muscular in 1 month? The best way 💉"
    ],
    [
        "-l5dYIrnHnE",
        "Abstinence and attractiveness. I got it all!"
    ],
    [
        "lk9D7Pi0U9U",
        "Как система отупляет людей? Смотри пока не удалили"
    ],
    [
        "D4mwj-Od4SY",
        "Как я стал падальщиком? Главная ловушка для мужчин в отношениях. Мужское движение"
    ],
    [
        "yuwNT8Ndles",
        "Главный принцип мышечного роста. Всем ботаникам посвящается"
    ],
    [
        "uvWHg5mHrTE",
        "Мастурбация создана для идиотов"
    ],
    [
        "3uROipeNXec",
        "Как я стал психологом совершенно случайно ?"
    ],
    [
        "_Nqb0OZ8czo",
        "Как перестать быть падальщиком, аленем и баборабом навсегда? Мой авторский способ. Лучший способ"
    ],
    [
        "6p2R0Km54zs",
        "Моё новогоднее выступление 🎉Единственное правильное поздравление которое можно пожелать мужчине 🔥"
    ],
    [
        "89nRIVo21J0",
        "Как система уничтожает мужчин. Экстренный выпуск. Запретили делать присед"
    ],
    [
        "_4xv6Bx_Tuo",
        "Высшие силы существуют. Доказательство. Вселенная устроила с меня спрос моментально"
    ],
    [
        "H1foj3oyVE4",
        "Вся людская сущность в одном видео. Всё печально"
    ],
    [
        "drt-OFyloJA",
        "Деньги, счастье, свобода, испытания, аленизм, сила духа. Большой подкаст"
    ],
    [
        "EY9hGAHPato",
        "Стоит ли идти в армию чтобы стать настоящим мужчиной? Французский иностранный легион"
    ],
    [
        "rZrypLbLfOQ",
        "Watch this when you're ready to give up. I'm homeless now. Going into seclusion. Never give up"
    ],
    [
        "pz0A9xnsXBM",
        "You must suffer to become a man. Anti-Alenism. Men's movement."
    ],
    [
        "B3O8lCRih6k",
        "Аленизм. Пролактин. Мужское движение. Как я прозрел за 5 минут благодаря Ford Mustang 🚗 ? Очнитесь"
    ],
    [
        "YLRsNNWXRZk",
        "Прокачиваю манипуру чакру. Жестокий спорт в 4 утра, закаливание в ледяной воде, голодание."
    ],
    [
        "nZ20Tq_XNWs",
        "You have to do sports🏅otherwise life will punish you very severely! Don't play with fate."
    ],
    [
        "rPxl_hYM4As",
        "Очистка мозгов от информационного мусора. Разбиваю телевизор"
    ],
    [
        "1Fy6c8tljEs",
        "Тренировка груди на брусьях 🔱Zyzz жив 🔱 тело как у древнегреческих Богов"
    ],
    [
        "qMY36T3Osuk",
        "Как Сатана хочет вас погубить. Сила духа. Страха нет. Ты должен быть сильным"
    ],
    [
        "S1yuJUU8wsA",
        "Ты не имеешь права быть слабым в этом гнилом мире. Страха нет"
    ],
    [
        "AVI5DbXX03g",
        "My back workout on the pull-up bar 🔱 Zyzz is alive 🔱 Getting a physique like an ancient Greek god"
    ],
    [
        "2hmDdfYiRbU",
        "Who is Voronovich?"
    ],
    [
        "BG8FbwqbJoo",
        "Prayer against divorce 🤣 the priest is shocked. Royal scarlet. Prolactin drives people crazy."
    ],
    [
        "3KwDu2CcmLw",
        "Кто такой альфа ? High value man. 3-я часть"
    ],
    [
        "wdKNYg983Ug",
        "Что такое альфа-самец? High value man. Вторая часть."
    ],
    [
        "1ET2CB21ZaE",
        "Чем отличается альфа от аленя? Вы ошибались"
    ],
    [
        "bqIzk9Z2ToE",
        "My signature method for meeting girls on the street"
    ],
    [
        "mu86ckGSM60",
        "Только таких мужчин женщины любят, уважают и боятся потерять. Падальщики и алени проходят мимо"
    ],
    [
        "H2m2QiPm7Rc",
        "The simplest and only way to survive a breakup. Restore energy, heal the psyche."
    ],
    [
        "lN3Bh0L1Ubg",
        "A Million Dollar Tip: How Your Home Affects Your Life and How to Attract Success"
    ],
    [
        "_H9X87u63c8",
        "Sexual abstinence and success in life. What is talent from a spiritual perspective? How to attrac..."
    ],
    [
        "HPEkIRFCnss",
        "Восстановление психического здоровья. Исцеление себя"
    ],
    [
        "hHnzOHWuToE",
        "Женщин тошнит от хороших парней. Ответ подписчику. Пролактин и привлекательность"
    ],
    [
        "rOFcwzPbqUM",
        "С чего начинается духовное развитие ? Ответ подписчику. Пирамида мужского развития"
    ],
    [
        "aOwS59COAts",
        "Общество делает из тебя никчёмного, жалкого червя. Задумайся. Реальный пример из жизни"
    ],
    [
        "eOJ7TegJKmI",
        "A terrifying relationship story. You'll never hear a more terrifying one."
    ],
    [
        "qR9siiEjCKE",
        "Saving a subscriber from suicide. The fastest way out of depression. Dopamine fasting."
    ],
    [
        "NKUyFnJiIFw",
        "Как быстро выучить любой иностранный язык ? Становлюсь полиглотом"
    ],
    [
        "aJuIBeEtZPY",
        "Resetting Your Dopamine System. Enjoy Every Second of Life!!!"
    ],
    [
        "m-umjmTEYW0",
        "Дегенеративный образ жизни. Очнись пока не поздно! Восстанавливаем дофаминовые рецепторы"
    ],
    [
        "5ICIY1kk7E0",
        "The first sign of low energy"
    ],
    [
        "NEjTHPE15pc",
        "Отшельничество, единение с природой, гармония"
    ],
    [
        "MIoLs8VRukA",
        "Шизофрения. Почему во Франции так много психически больных. Береги голову с молоду"
    ],
    [
        "4QRIO5vKHZ8",
        "Сайты знакомств это зло"
    ],
    [
        "p7AS4WhH648",
        "Negative emotions ruin your life. And here's my most important advice!"
    ],
    [
        "WZt0oGxwTrc",
        "Ты забудешь что такое одиночество и скука. Чем  я занимаюсь днями"
    ],
    [
        "5BCFiDwVsPI",
        "Как бороться с депрессией? Причины депрессии. Хватит деградировать"
    ],
    [
        "lr1goWqnCEQ",
        "Нужно жить свою жизнь здесь и сейчас"
    ],
    [
        "K2EmZDaHI-8",
        "Self-development always begins with sexual abstinence!"
    ],
    [
        "ktox2LKMAHE",
        "Твоя жена хочет переспать с массажистом"
    ],
    [
        "mv4a2ypub1E",
        "Деньги приводят к деградации. Хватит гнаться за бабками, начни жить здесь и сейчас"
    ],
    [
        "QvB9t0m1i5g",
        "Signs of fate, warnings from the universe. Everything happens for the best."
    ],
    [
        "9B-jyQb5bYs",
        "The only way to be happy. Dopamine, psyche, happiness, vitality"
    ],
    [
        "OdfBRFHKSC8",
        "Вся женская сущность в одном видео. Измены, любовники, разводы. Психология отношений"
    ],
    [
        "cxQuhUQlHU0",
        "Как мастурбация полностью сломала мою жизнь. Половое воздержание"
    ],
    [
        "UnpopYbe1IU",
        "Why relationship psychology is a useless topic"
    ],
    [
        "70S6Hxg2V3A",
        "Общество вырождается и деградирует. Век удовольствий, общество потребления"
    ],
    [
        "7BsZ7oqafow",
        "В отношениях у тебя существует только две роли. Психология отношений"
    ],
    [
        "wWJL9nytBD8",
        "Основное отличие мужчины и женщины. Психология отношений"
    ],
    [
        "SJA4-R6Rfrc",
        "Воздержание и привлекательность. Страх отказа"
    ],
    [
        "5WI8IBLi8Fo",
        "Влияние замкнутого пространства на психику. Депрессия"
    ],
    [
        "sDRNI8b9bbQ",
        "Как правильно ссориться с девушкой? Психология отношений. Баланс значимости"
    ],
    [
        "KbEpvgjH9Mc",
        "The Dopamine System. Where Does Depression Come From? Sexual Abstinence"
    ],
    [
        "525QrDOrJSg",
        "Как довести женщину до оргазма. Основной принцип"
    ],
    [
        "Wop78apvITw",
        "Новый формат канала.  баборабство, зависимости, сила духа"
    ],
    [
        "T8Gr0dzHHro",
        "Никогда не позволяй бабе оценивать тебя. Продолжение"
    ],
    [
        "WZjDvkoHM6c",
        "Никогда не позволяйте бабе вас оценивать"
    ],
    [
        "q7X5AtVeprc",
        "Ранги в отношениях. баланс значимости. как ранг влияет на привлекательность"
    ],
    [
        "GxEvKiFIUMA",
        "Всеобщая деградация. Баборабство, аленизм. Мужики очнитесь"
    ],
    [
        "HqHdfuRMtCg",
        "Why Women Should Be Pursuing Men"
    ],
    [
        "Ojx77hdgIFk",
        "женщины умнее мужчин (в большинстве случаев)"
    ],
    [
        "R6cMy_xXZYs",
        "Почему раньше было меньше разводов"
    ],
    [
        "fLQ8CemlhYg",
        "Почему женщины всегда предают своих мужчин?"
    ],
    [
        "UwNv9CuWH1Q",
        "Как женщины тестируют своих мужчин?"
    ],
    [
        "8dV10RtGiZk",
        "Действительно ли у всех женщин в приоритете деньги? Психология отношений"
    ],
    [
        "LQ4DunKIukk",
        "Infantilism Is Our Greatest Enemy"
    ],
    [
        "YmqGXF6pBW8",
        "What is the meaning of life?"
    ],
    [
        "ST-Xyc9Tz9A",
        "Эпидемия лизунов 😛"
    ],
    [
        "663xDspMM-0",
        "Что привлекает женщин больше всего"
    ],
    [
        "ocmT4zt8aK0",
        "What Women Dream About"
    ],
    [
        "mV9POVc7FvA",
        "Женщины кастрируют своих мужчин. Продолжение"
    ],
    [
        "1Ar9JbIpVWk",
        "A woman doesn't know how to love. Suitable and unsuitable women."
    ],
    [
        "TEHhXonaEYo",
        "Все женщины врут. Раскрываю женскую сущность"
    ],
    [
        "Ez1wwnhsvRY",
        "Alenism and baborabism in the modern world. Continued"
    ],
    [
        "iTq8_MovTXE",
        "Эпидемия аленизма. Упадок мужественности в современном мире"
    ],
    [
        "SOV1pWBlCiI",
        "The main problem with all \"psychologists.\" Why their relationship advice doesn't work."
    ],
    [
        "3fVs-x9zt10",
        "Как женщины кастрируют своих мужчин. Зачем они это делают"
    ],
    [
        "NBpSPjdVGF8",
        "How parents ruin their children's lives. It's scary."
    ],
    [
        "XGibuVI0TIQ",
        "Мужская энергия и откуда берутся лесбиянки"
    ],
    [
        "Bg7O5VV-PuY",
        "Откуда возникает притяжение между мужчиной и женщиной. Мужская энергия"
    ],
    [
        "1XJzYht0OgA",
        "«Лучшая» работа во Франции , доступна всем, не нужны даже документы"
    ],
    [
        "Ctx0bN66Q8k",
        "Лучшее упражнение чтобы нравиться женщинам"
    ],
    [
        "-2ze5WAm-pg",
        "Криминал в Марселе. Попадаю под раздачу"
    ],
    [
        "7E75tslW48E",
        "Почему не существуют отношения длинною в жизнь. Не верьте в сказки"
    ],
    [
        "QRG_oE-yFeE",
        "NEVER listen to relationship advice from women!"
    ],
    [
        "a3l_Tt6QacY",
        "Нужны ли деньги при построении отношений с женщинами?"
    ],
    [
        "TKkah6BmzmU",
        "Never tell a woman this. A one-way ticket to a breakup"
    ],
    [
        "8sVcKNV7Ibc",
        "Нужна ли семья современному мужчине?"
    ],
    [
        "sDgJrlOvI2Q",
        "The harm of masturbation"
    ],
    [
        "8tLNGNxsBIU",
        "Основной принцип взаимодействия с женщиной. Психология отношений"
    ],
    [
        "AWJTcraR8HU",
        "My Dumbest Relationship Mistakes: A Dissection of Alenism"
    ],
    [
        "KXO8_WN7Tgg",
        "Как влюблять женщин? Второй этап"
    ],
    [
        "vGrA0OfKX0Y",
        "Как женщины пытаются прогибать мужиков и манипулировать"
    ],
    [
        "RHKeKRIP0-Q",
        "Что привлекает женщин в плане внешности? Моё исследование"
    ],
    [
        "hk9oonglKg4",
        "Главная ошибка в отношениях с женщинами"
    ],
    [
        "SNWWXoiUzSE",
        "How to communicate with women online? My tactics. The basic principle"
    ],
    [
        "3chL2V-3Sbg",
        "Чем опасна фраза «я не даю на первом свидании» (Прямой путь во фрэндзону)"
    ],
    [
        "Isl0bR-M2QU",
        "Как влюбить женщину на первой встрече? Продолжение. Основной момент"
    ],
    [
        "_-46abRo2mQ",
        "How to make women fall in love on the first date? My tactics"
    ],
    [
        "62t38l_M9Kw",
        "Главный минус французских женщин"
    ],
    [
        "Kv43wPQnMqI",
        "The most important point when meeting people on Tinder, Badoo, etc. in Europe. A must-see."
    ],
    [
        "8qYclfVe5wU",
        "The worst lie men believe. And why love ends."
    ],
    [
        "W5oT532bLB0",
        "Моя самая главная ошибка в жизни. О чем жалею больше всего"
    ],
    [
        "yZDYL1k_FIw",
        "How to find a wife in France to get residency? What is the difference between French women and Sl..."
    ],
    [
        "kXhp1ZiaVbw",
        "Manifestations are instantaneous"
    ],
    [
        "tHmrGf9XJI4",
        "VORONOVICH is live!"
    ],
    [
        "PAPDHYYPsBc",
        "PROFESSOR VORONOVICH is live!"
    ],
    [
        "IYmbHxr-TKg",
        "ПРОФЕССОР ВОРОНОВИЧ СТРИМИТ"
    ],
    [
        "DVRpp1MT0XU",
        "My channel is three years old!! My journey from the swamp to success!"
    ],
    [
        "BIDCamOtZf8",
        "Мои главные ошибки в отношениях"
    ],
    [
        "pgniIrUztFg",
        "купил комп чтобы читать рэп"
    ],
    [
        "bGt_ZF2PzVk",
        "The essence of my activity"
    ],
    [
        "1LXu6uoj2Ps",
        "Кончелыжный образ жизни"
    ],
    [
        "Bw6SfMcYrn0",
        "Моё понимание Бога"
    ],
    [
        "W_IUwfG6bsc",
        "Ответы на вопросы"
    ],
    [
        "jzW86NvLrhk",
        "Проиграл войну против нечисти"
    ],
    [
        "jcCKCmNZSks",
        "Новый этап в творчестве. Анонс закрытого канала"
    ],
    [
        "ezQ6V96w8X0",
        "Жизнь научила разбираться в людях"
    ],
    [
        "GChfKe0iwAc",
        "Закон бумеранга и гниль человеческая"
    ],
    [
        "_2MDz-1VXJQ",
        "Трансерфинг реальности. Как я чуть не материализовал мечту всей жизни"
    ],
    [
        "tipq-LZueQs",
        "Чудеса в моей жизни. Важнейший стрим за всю историю канала"
    ],
    [
        "HV2f77H4SDo",
        "Случайности не случайны"
    ],
    [
        "44MylHB8uJ0",
        "Стрим. Ответы на вопросы"
    ],
    [
        "6DDT_C-a7f0",
        "Стрим. Ответы на вопросы"
    ],
    [
        "4ZNerdhWN6U",
        "Загадочный случай с темной энергией. Стрим"
    ],
    [
        "HXCGwD23bW4",
        "Ответы на вопросы"
    ],
    [
        "0hPnbxj7Ybg",
        "САМЫЙ СЛАБЫЙ ШКОЛЬНИК В США"
    ],
    [
        "SFZimHwQGi4",
        "Париж опасный город!!!!"
    ],
    [
        "BLM9WPWztjw",
        "I stretch my facial bones to get nice cheekbones. Luxmaxing"
    ],
    [
        "b3dTWXBz7mQ",
        "БЛЭКПИЛЛ головного мозга"
    ],
    [
        "_FX4mhLhLsg",
        "Only such a business will bring happiness into your life."
    ],
    [
        "LEoQzy-hrbI",
        "Так звучит подход после расставания"
    ],
    [
        "WmaZ6JqPnX8",
        "This is how business starts"
    ],
    [
        "v5Sqqz6YrCQ",
        "Gratitude practice"
    ],
    [
        "o8d2Hip0tb8",
        "Поменял внешность #blackpill"
    ],
    [
        "POiOQLNsNU8",
        "How does a girl see your rank? Relationship psychology"
    ],
    [
        "SHecWzVWucg",
        "УЛУЧШИТЬ ВНЕШНОСТЬ ЗА МИНУТУ"
    ],
    [
        "jBc93lE8Ucg",
        "What is BLACKPILL?"
    ],
    [
        "xZvkVFbvquQ",
        "Встретил Рони Колемана 💫"
    ],
    [
        "zpVUuGBl4sY",
        "Don't think, just DO"
    ],
    [
        "PvukURHRPmw",
        "Where do money and wealth gravitate?"
    ],
    [
        "dzwy78KEsDE",
        "Competition in the modern world"
    ],
    [
        "Gmy_nVSsoec",
        "Girls destroy weak men"
    ],
    [
        "ePkNA2vSRow",
        "Women can smell you right through."
    ],
    [
        "sNuHo3KykCA",
        "Нельзя помогать таким «друзьям»"
    ],
    [
        "5B9uxYbWPlA",
        "Перестань общаться с нормисами"
    ],
    [
        "02Y03Gh93zM",
        "Боязнь знакомиться с женщинами"
    ],
    [
        "UZiciWyWPFM",
        "The Law of Tithing is Wealth"
    ],
    [
        "dxmzRdhKqK8",
        "Американские ценности. Пикник на обочине"
    ],
    [
        "Qa4qhQiBSOc",
        "Качалка реально отупляет"
    ],
    [
        "uLILLT_DB6c",
        "Передоз фармой в прямом эфире"
    ],
    [
        "giKDR1MpdaA",
        "Пацаны когда бросила тёлка"
    ],
    [
        "Aw8nchFWHdg",
        "Пацаны после расставания"
    ],
    [
        "-TDYjz-AXfc",
        "What is love?"
    ],
    [
        "ycLkFCvBRGs",
        "Встретил деда 🔱🔱🔱"
    ],
    [
        "Y-Dhp-Z8YJQ",
        "Met Mokshin. Podcast coming soon"
    ],
    [
        "KqWGmhxecjA",
        "Мысли материальны. Мечты сбываются"
    ],
    [
        "l8Y-PpWrtSc",
        "Сын депутата унижает на дороге"
    ],
    [
        "IsJYTIvU-Hg",
        "Сын депутата устроил беспредел на улицах"
    ],
    [
        "lzvrC--jleE",
        "Сын депутата в Голливуде"
    ],
    [
        "6w1rx8kseBQ",
        "Dental health is EASY! Whitening at home!"
    ],
    [
        "0_h1z8L2S4E",
        "ЛУЧШЕЕ ПРИРОДНОЕ ЛЕКАРСТВО"
    ],
    [
        "TiP_ps8aKs4",
        "ВСЕГДА ОСТАВЛЯЙ ЧАЕВЫЕ! КЛЮЧ К БОГАТСТВУ!"
    ],
    [
        "vfsymlAd3tg",
        "NEVER BE JEALOUS OF ANYONE!"
    ],
    [
        "Zu5KKnsIrqU",
        "best nutrition advice"
    ],
    [
        "sfr8huzNLWk",
        "FORGET WHAT IT IS TO BE SICK!!!"
    ],
    [
        "Jv_OxTA87JQ",
        "People look at me like I'm a BASTARD. But I enjoy it!!"
    ],
    [
        "TNUy2cEF8Vs",
        "Cool life hack for health!"
    ],
    [
        "L6owDHmj7nw",
        "Богатая милфа решает"
    ],
    [
        "Ln5kmioj9TI",
        "Помолодел. Не такой еще старый как думал"
    ],
    [
        "H1mQsjpi8fQ",
        "В натураху"
    ],
    [
        "hkQmlqCUvcU",
        "Подняться можно на ВСЁМ!"
    ],
    [
        "6zHARo-7gBc",
        "животное"
    ],
    [
        "m9Za9-KmdVU",
        "ТВАРЬ"
    ],
    [
        "iZuZnUEe-tI",
        "время летит.. сколько еще осталось?"
    ],
    [
        "2WDoS8dh03U",
        "Got scammed out of $2000 because of this..."
    ],
    [
        "4DkOwXcLqwg",
        "Fighting baldness. Will I succeed?"
    ],
    [
        "sCakM0XEffg",
        "The Heart Chakra in Our Lives"
    ],
    [
        "1VG2WUsCb7s",
        "все пацаны когда бросила тёлка (("
    ],
    [
        "mcbJLsO4f-k",
        "лучшая замена приседаниям со штангой"
    ],
    [
        "QjPVbo8fnBw",
        "Качаюсь без химии"
    ],
    [
        "166TjYa3MnQ",
        "Финал ЧМ 2022. Отморозки. Околофутбол"
    ],
    [
        "B0dHgNmObQ0",
        "Отбиваю мозги молодому. (мне уже отбили)"
    ],
    [
        "tUguzG4WJQ4",
        "Девушки дают без проблем"
    ],
    [
        "mtvvPjKVMZ8",
        "Я ненавижу стероиды"
    ],
    [
        "owXWJ2Iyv4o",
        "Тянем с паузой без читинга 😅"
    ],
    [
        "s959mmMltpU",
        "Тянем детские веса"
    ],
    [
        "PFbIPfdbWZE",
        "Бицуха оставляет желать лучшего"
    ],
    [
        "5PDDRap7WRA",
        "Our Fears Always Come True"
    ],
    [
        "uEGSIW8cA3k",
        "Treason"
    ],
    [
        "fBcfX3_DmLw",
        "Тупо дрыщ. За то в натураху!!"
    ],
    [
        "TwlhpvOhIDk",
        "Мы ничтожество для женщин"
    ],
    [
        "f8zw1WoBkzM",
        "Тебя никто не любит! Ты нигде не нужен"
    ],
    [
        "nwJZoXOrNR4",
        "Измена в прямом эфире !!!"
    ],
    [
        "R_El047Jq7U",
        "Френдзона"
    ],
    [
        "kp5bnLseN2Q",
        "Никакой химии !!! Только натураха"
    ],
    [
        "mayvU2drX_M",
        "Моя форма внатурашку (я дрыщ)"
    ],
    [
        "1h7kasB6eEk",
        "Девушка тебе не принадлежит !!!"
    ],
    [
        "CF5e4yzfGZo",
        "Женские чары ОПАСНЫ !!! Очень опасны"
    ],
    [
        "8q2_4JnticU",
        "Почему девушка бросила тебя ?"
    ],
    [
        "Z1NJ3XqtQqc",
        "женщины это манипуляторши от Бога !!!"
    ],
    [
        "Lvd0BayafMI",
        "Девушка тебе не принадлежит. Измены и развод"
    ],
    [
        "uAmZLcs09wQ",
        "Why does an ex-girlfriend come back?"
    ],
    [
        "MoVb5ct72o4",
        "Моя форма на половом воздержании. Тестостерон и целибат"
    ],
    [
        "h_uvMOp83ok",
        "Мастурбация убивает. Каждый акт онанизма это страшная травма"
    ],
    [
        "dNCRIx2vYCQ",
        "Дельты с читингом ))"
    ],
    [
        "CI5Mj11qJy8",
        "Как улучшить свой вид в качалке ? Крутой лайфхак"
    ],
    [
        "HQASpXiW6K8",
        "ДЕВУШКА ТОЧНО ТЕБЯ БРОСИТ ЕСЛИ…"
    ],
    [
        "NvJTQLkboJI",
        "Female infidelity. Reasons"
    ],
    [
        "SpeOaNoS3-o",
        "Низкий ранг в отношениях с девушками"
    ],
    [
        "FhqhZlZCyEo",
        "Мужская база. Ранги в отношениях с женщинами"
    ],
    [
        "V_A_QKS_wqY",
        "Воздержанец"
    ],
    [
        "lAx1WCzRNcs",
        "Men's Base. Breaking Up with a Girlfriend"
    ],
    [
        "HhtuPGfKO8s",
        "Моя форма внатураху"
    ],
    [
        "jl9J59s88cU",
        "Мужская база. Пикап и знакомства"
    ],
    [
        "_Dx0oj7e_AE",
        "Male base. Testosterone"
    ],
    [
        "zqOrO_IOg7s",
        "Магия утра. Халявная энергия"
    ],
    [
        "GJHUJ9VBj-k",
        "How to propose 🔥"
    ],
    [
        "Gf1M_yklLkU",
        "Running attracts SUCCESS into your life"
    ],
    [
        "7XcguPaXwUc",
        "WHY RUN IN THE RAIN?"
    ],
    [
        "ql49v_k7uGA",
        "ГЛАВНЫЙ ВРЕД МАСТУРБАЦИИ"
    ],
    [
        "6z_7XClV3F8",
        "PSYCHOLOGY OF RELATIONSHIPS IN SIMPLE WORDS"
    ],
    [
        "6T2inJwsFHs",
        "ЭТОГО МОЖНО ДОБИТЬСЯ БЕЗ СТЕРОЙДОВ"
    ],
    [
        "RqbFq_8tKeo",
        "NEVER PICK UP A WOMAN FROM A DATING SITE"
    ],
    [
        "6VBvcQNd1GQ",
        "РАЗОБЛАЧЕНИЕ ВЕРДИКТА. Критерий пригодности не работает"
    ],
    [
        "DoRRS2Jhhsg",
        "РАЗОБЛАЧЕНИЕ ВЕРДИКТА. Тотальный игнор не работает"
    ],
    [
        "Yk5zaioiplQ",
        "СКОЛЬКО Я ЗАРАБАТЫВАЮ С 1400 ПОДПИСЧИКОВ"
    ],
    [
        "iHyQcK0PBY4",
        "НИКОГДА НЕ ТРАТЬ ДЕНЬГИ НА БАБУ"
    ],
    [
        "HfGIFFb4a3U",
        "Как стать счастливым за месяц? Деньги не нужны"
    ],
    [
        "-gv6KTTSp1o",
        "The Biggest Gym Mistake ⛔️"
    ],
    [
        "hTp7egXgK2g",
        "The secret to a perfect physique all year round"
    ],
    [
        "6z6R3gMV6qQ",
        "Your woman is always actively searching."
    ],
    [
        "-sp5odfGUwA",
        "Living a life of abstinence. Sexual abstinence brings joy to life even when you're broke."
    ],
    [
        "lrWiGEUn1Bo",
        "Самый верный способ потерять свою девушку"
    ],
    [
        "YmgBv4uZ3hM",
        "Главный плюс полового воздержания"
    ],
    [
        "rgAge1lWSUQ",
        "Всё еще веришь в любовь? Спешу тебя огорчить"
    ],
    [
        "VgqPzQnK5nc",
        "Типичный вечер в моем гетто"
    ],
    [
        "yL71pGSP5YY",
        "Цыганский рынок в Марселе"
    ]
]

def get_transcript(video_id):
    try:
        # Проверяем версию библиотеки и вызываем нужный метод
        if hasattr(YouTubeTranscriptApi, 'list_transcripts'):
            # Версии ~0.4.x до 1.x
            transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        elif hasattr(YouTubeTranscriptApi, 'get_transcript'):
            # Очень старые версии < 0.3.x
            transcript_data = YouTubeTranscriptApi.get_transcript(video_id, languages=['ru', 'en'])
            text = " ".join([item['text'] for item in transcript_data])
            text = text.replace('\n', ' ')
            return text
        else:
            # Версия >= 1.2.x (текущая)
            ytt_api = YouTubeTranscriptApi()
            transcript_list = ytt_api.list(video_id)

        # Ищем транскрипт на русском (созданный вручную или автоматически)
        try:
            transcript = transcript_list.find_transcript(['ru'])
        except Exception:
            try:
                 # Если русского нет, берем английский и переводим
                 transcript = transcript_list.find_transcript(['en']).translate('ru')
            except Exception:
                 # Если и это не вышло, берем первый попавшийся и переводим
                 first_transcript = list(transcript_list)[0]
                 transcript = first_transcript.translate('ru')

        # Получаем данные субтитров
        transcript_data = transcript.fetch()

        # Форматируем в чистый текст
        formatter = TextFormatter()
        text = formatter.format_transcript(transcript_data)

        # Убираем лишние переносы строк
        text = text.replace('\n', ' ')
        return text
    except Exception as e:
        return f"Не удалось получить текст: {e}"

def main():
    output_file = 'voronovich_knowledge_base.txt'

    total_videos = len(VIDEOS)
    print(f"Найдено {total_videos} видео для обработки. Начинаем парсинг...")

    with open(output_file, 'w', encoding='utf-8') as out_f:
        for index, (video_id, title) in enumerate(VIDEOS, 1):
            print(f"[{index}/{total_videos}] Скачиваю субтитры для: {title}")

            transcript_text = get_transcript(video_id)

            # Записываем заголовок
            out_f.write(f"--- Видео: {title} ---\n")
            # Записываем текст
            out_f.write(transcript_text + "\n\n")

            # Чтобы YouTube не заблокировал за спам, делаем небольшую паузу
            time.sleep(random.uniform(1.0, 3.0))

    print(f"Готово! База знаний успешно сохранена в файл {output_file}")

if __name__ == '__main__':
    main()
