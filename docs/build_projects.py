"""Builds docs/projects/<slug>.html case-study pages in the portfolio design.
Edit the PROJECTS data below and run:  python docs/build_projects.py"""
import html, os
OUT = os.path.join(os.path.dirname(__file__), "projects")
HOME = "https://rural-lunch-f54.notion.site/40d35114c675811b92afe36f58b0b3b5"
RAW = "https://raw.githubusercontent.com/Seema777111-git/Saki-AI-Portfolio/main/"
CDN = "https://cdn.jsdelivr.net/gh/Seema777111-git/"
E = html.escape

PROJECTS = [
 dict(slug="ReviewLens", icon="🔍", name="ReviewLens", cat="AI data analysis",
  promise="Turn customer reviews into clear, actionable insights in seconds.",
  summary="Upload reviews as a CSV and ReviewLens reads every one. It tags sentiment, category and urgency, then shows the top pros and cons, critical issues and a weekly insights report on one dashboard.",
  status="Working demo", tech=["Python","Streamlit","LangChain","Pydantic","Pandas","LLM integration"],
  links=[("🌐 Live demo","https://reviewlens.royalseemah.tech/"),("GitHub","https://github.com/Seema777111-git/ReviewLens")],
  videos=[("Demo", CDN+"Saki-AI-Portfolio@1e8349b/ReviewLens/demo/reviewlens-demo.mp4","Walkthrough of the app using synthetic demo data")],
  problem="Popular products and businesses collect <b>thousands of reviews</b>, and nobody has time to read them all. Important feedback stays hidden in long, messy text, and star ratings alone don't explain <i>why</i> customers are happy or unhappy.",
  solution=[("Every review tagged","sentiment, category, urgency and language"),("Validated AI output","LangChain with Pydantic structured responses"),("Weekly insights report","positive themes, recurring complaints, critical issues and three recommended actions"),("High-urgency alerts","plus a suggested reply for each review"),("English, Tamil and Tanglish","reviews supported")],
  screens=[RAW+"ReviewLens/images/screen-1-input.jpg",RAW+"ReviewLens/images/screen-2-dashboard.jpg",RAW+"ReviewLens/images/screen-3-reports.jpg"],
  infographic=RAW+"ReviewLens/ReviewLens-infographic.jpg",
  how=["<b>Outputs</b>: an interactive dashboard with KPI cards and filters, an enriched review table, and a CSV export that opens in Excel","<b>Who it is for</b>: restaurants, food delivery, e-commerce and hospitality businesses"],
  safeguards=["Synthetic demo data, so no real customer information is used","Human review for high-urgency cases","Prompt-injection protection"],
  value=[("⏱️","Saves reading time","Every review read and summarised for you."),("🎯","Fix the right things","Recurring complaints ranked first."),("🚨","Act on urgent issues","High-urgency reviews flagged fast.")],
  note="All demo companies and reviews are synthetic data."),

 dict(slug="BizRadar-AI", icon="🎯", name="BizRadar AI", cat="Market research",
  promise="Know your market in about a minute.",
  summary="Enter a business idea, a city and a target customer. Five AI agents research the live web and return a sourced market report: competitors and their prices, customer complaints, market gaps, positioning and a 30-day launch plan.",
  status="Working demo (private testing)", tech=["Python","Streamlit","PostgreSQL","Redis background worker","Docker","GPT-4o-mini","Serper search"],
  links=[("Technical guide (PDF)","https://github.com/Seema777111-git/Saki-AI-Portfolio/blob/main/BizRadar-AI/docs/TECHNICAL_GUIDE.pdf")],
  videos=[("Demo · 2 min 57 s", CDN+"Saki-AI-Portfolio@ca7cab1/BizRadar-AI/demo/bizradar-ai-demo.mp4","Real research runs recorded in the app, narrated")],
  problem="Before a new business launches, someone has to study the competition. A marketing intern typically spends <b>2 to 3 days</b> searching websites, maps and reviews and copying it into Excel. The result has no sources and goes out of date quickly.",
  solution=[("Five AI agents","Manager, Market Researcher, Review Analyst, Strategy Analyst, Report Writer"),("Proof for every claim","each price links to its source page and date"),("Honest labels","Fact, Estimate, Inference or Unknown"),("Built for India","Google Maps, Justdial, Swiggy, Zomato, IndiaMART and more, prices in ₹"),("Never overspends","hard limits on tokens, pages, searches and time")],
  results_title="Real research runs", results_table=(["Business idea · city","Sources","Platforms","Time"],[["Kids AI coding classes · Coimbatore","<b>79</b>","6","1 min 05 s"],["Organic vegetable box · Mysuru","<b>86</b>","5","58 s"],["Coworking café for students · Kochi","<b>70</b>","6","—"]]),
  infographic=RAW+"BizRadar-AI/BizRadar-AI-infographic.png",
  how=["<b>Outputs</b>: a 9-section report on screen, PDF and Markdown downloads, a pitch deck, and weekly alerts when a rival changes","<b>Who it is for</b>: first-time founders, small business owners watching rivals, consultants and agencies"],
  value=[("⚡","Days become a minute","Market research in about a minute."),("🔗","Every claim checkable","Prices and claims link to their source."),("📅","Ready to act","Positioning and a 30-day launch plan.")],
  note="Source code is private; a walkthrough is available on request."),

 dict(slug="DataSherpa-AI", icon="📊", name="DataSherpa AI", cat="AI data analysis",
  promise="An AI data analyst for small businesses, with answers you can trust.",
  summary="Upload a sales file, ask “Why did sales drop last month?”, and receive a formal report with key numbers, charts, possible reasons and next steps.",
  status="Working demo", tech=["Python 3.11","FastAPI","pandas","PostgreSQL","React + TypeScript","Docker","Microsoft Agent Framework","OpenAI"],
  links=[("Technical guide (PDF)","https://github.com/Seema777111-git/Saki-AI-Portfolio/blob/main/DataSherpa-AI/docs/TECHNICAL_GUIDE.pdf")],
  videos=[("Demo · about 4 min", CDN+"Saki-AI-Portfolio@main/DataSherpa-AI/demo/DataSherpa-AI-demo.mp4","From sign-in to the approved report, narrated")],
  problem="Small business owners have sales data in spreadsheets but no analyst. General AI chatbots can produce convincing numbers that are wrong, which is not acceptable for business decisions.",
  solution=[("The AI never does the maths","numbers come from executed calculations"),("Checked twice","a mismatch blocks the answer"),("Data Quality Guardian","explains duplicates and bad values first"),("Facts kept apart from guesses","labelled “not proven”"),("Human in control","nothing is final until approved")],
  results_title="Results (demo data)", stats=[("24/24","known answers correct"),("84/84","verification checks passed"),("6/6","reproducible runs"),("260+","automated tests")],
  infographic=RAW+"DataSherpa-AI/DataSherpa-AI-infographic.png",
  how=["<b>Smart router</b>: cached answers use no AI tokens, standard questions use a verified Python engine, and only custom questions use the full agent loop","<b>AI agent team</b>: Planner → Coder → Sandbox → Verifier → Reviewer → Advisor → human approval","<b>Safe execution</b>: AI-written code runs in a locked-down Docker sandbox with no internet access and strict limits","<b>Security</b>: bcrypt passwords, rotating refresh tokens, rate limiting and per-user data isolation"],
  value=[("📈","Analyst-level insight","From the owner's own data."),("✅","Every number verified","Calculated, then checked twice."),("🧑‍💼","Owner in control","Nothing is final until approved.")],
  note="Source code is private; a walkthrough is available on request."),

 dict(slug="SmartCater-AI", icon="🍽️", name="Smart Cater AI", cat="Sales automation",
  promise="From enquiry to quotation, on autopilot.",
  summary="An AI agent answers a catering client's questions in chat and collects the event details. Automation then records the lead, books a consultation, asks the owner to approve and emails a professional quotation, with no manual chasing.",
  status="Working demo", tech=["n8n","Google Gemini AI agent","Telegram","WhatsApp","Tally forms","Supabase","Gmail","Google Calendar","PDF generation"],
  links=[("GitHub overview","https://github.com/Seema777111-git/Saki-AI-Portfolio/tree/main/SmartCater-AI")],
  videos=[("Demo · 1 min 34 s", CDN+"Saki-AI-Portfolio@d57426d/SmartCater-AI/demo/smart-cater-ai-demo.mp4","One real enquiry, from the first chat message to the quotation PDF")],
  problem="Caterers receive enquiries on WhatsApp, Telegram, phone and forms. Messages are missed, quotations are typed by hand and follow-ups are forgotten, so bookings go to faster competitors.",
  solution=[("AI chat agent","answers questions and collects event type, date, guests, venue, food and budget"),("One lead database","in Supabase with a clear stage for every enquiry"),("Instant follow-up","confirmation email and a calendar invitation"),("Owner approval","before any price goes out"),("Itemised quotation PDF","with GST, emailed automatically")],
  results_title="The client journey", steps=[("Ask","Client chats with the AI agent on Telegram or fills a Tally form"),("Organise","The lead is saved in Supabase with its status"),("Connect","Confirmation email and consultation invite go out in seconds"),("Qualify","Interested leads move on; others are closed politely"),("Quote","Owner approves, and the quotation PDF is emailed"),("Track","Live pipeline view from enquiry to booked event")],
  infographic=RAW+"SmartCater-AI/SmartCater-AI-infographic.jpg",
  value=[("🕒","Answered 24/7","Every enquiry gets a reply."),("⚡","Quotes in minutes","Instead of hours of typing."),("✅","Owner approves","Every price, before it goes out.")],
  note="Source workflows are private; a walkthrough is available on request."),

 dict(slug="SlotEase", icon="📅", name="SlotEase", cat="Business software",
  promise="Online booking for salons, clinics and physiotherapy centres.",
  summary="Customers book a free slot in under a minute, with no app and no login. Owners run the day from one screen, and the system refuses double bookings.",
  status="Working product with demo data", tech=["React","TypeScript","Tailwind","FastAPI","SQLAlchemy","PostgreSQL 16","JWT + bcrypt","Docker","Caddy (HTTPS)"],
  price="₹499 per month per business, after a free trial", links=[],
  videos=[("🏠 Landing page", CDN+"Saki-AI-Portfolio@main/SlotEase/demo/SlotEase-1-landing.mp4","How SlotEase is presented to business owners"),("📊 Owner dashboard", CDN+"Saki-AI-Portfolio@main/SlotEase/demo/SlotEase-2-dashboard.mp4","Today, week view, stats, services and settings"),("📱 Customer bookings", CDN+"Saki-AI-Portfolio@main/SlotEase/demo/SlotEase-3-bookings.mp4","Booking at three different businesses")],
  problem="Appointment-based businesses take bookings by phone and WhatsApp. Two customers get the same slot, staff forget to record bookings, and there is no record of no-shows.",
  solution=[("A booking page per business","in its own colours"),("No double bookings","the database decides in one transaction"),("Owner dashboard","today, next customer, one-tap Done or No-show"),("Working hours with breaks","with clinic and salon presets"),("Each business sealed off","and this is tested")],
  results_title="Quality", stats=[("206","backend tests"),("38","end-to-end tests (Playwright)"),("0","serious or critical accessibility issues on all 11 screens"),("97 · 100 · 100","Lighthouse performance · accessibility · best practices")],
  infographic=RAW+"SlotEase/SlotEase-infographic.png",
  value=[("📅","No clashing bookings","Fewer missed appointments."),("📞","Less time on the phone","Customers book themselves."),("📊","Clear daily picture","At a simple monthly price.")],
  note="Source code is private; a walkthrough is available on request. All businesses and customers shown are demo data."),

 dict(slug="Hybrid-RAG", icon="🔗", name="Hybrid RAG", cat="RAG and search",
  promise="Ask questions about your documents and see exactly how each answer was built.",
  summary="Every PDF is indexed twice, as meaning-based vectors and as a knowledge graph of facts. Each answer is checked, scored and traced.",
  status="Working demo", tech=["Python","FastAPI","Streamlit","FAISS","sentence-transformers","NetworkX","OpenAI or Anthropic Claude","NVIDIA NeMo Guardrails","DeepEval","LangSmith"],
  links=[("GitHub","https://github.com/Seema777111-git/RAG/tree/main/rag-hybrid")],
  videos=[("Demo · 1 min 50 s", CDN+"Saki-AI-Portfolio@1e8349b/Hybrid-RAG/demo/hybrid-rag-demo.mp4","Real recording of the running application, with narration")],
  problem="Teams need answers from policies, contracts and manuals, but ordinary chatbots can invent facts and offer no way to check them. In business use, every answer must be traceable to its source.",
  solution=[("Two search methods","vector search plus a knowledge graph"),("Evidence with every answer","passages, facts, scores and timings"),("Guardrails","check the question and the answer, including grounding"),("Measured quality","with built-in evaluation")],
  results_title="Results", stats=[("77","automated tests"),("3","retrieval modes compared: hybrid, vector-only, graph-only"),("4","evaluation metrics: faithfulness, answer relevancy, contextual precision, contextual recall")],
  rag=dict(
   index=[("📄","Your PDFs","Policies, contracts, manuals"),("✂️","Chunking","Split into text chunks"),("🧮","Embeddings","sentence-transformers"),("🗂️","Two indexes","FAISS vectors + NetworkX knowledge graph")],
   query=[("❓","Question","Asked in plain language"),("🛡️","Input guardrail","NeMo Guardrails checks it"),("🔎","Hybrid search","Vector search + graph search"),("🧠","Grounded answer","OpenAI or Claude, from the evidence"),("✅","Output check","Grounding guardrail, scores, trace")],
   link=(3,2),
   concepts=[("✂️","Chunking","Long documents are split into small passages so the right part can be found."),("🧮","Embeddings","Each passage becomes a list of numbers that captures its meaning."),("🔎","Vector search","Finds passages with a similar meaning to the question, even with different words."),("🕸️","Knowledge graph","Stores facts and how they connect, for questions that need relationships."),("🛡️","Guardrails","Check the question before and the answer after, including grounding."),("📏","Evaluation","DeepEval scores faithfulness, answer relevancy, contextual precision and recall; LangSmith traces each run.")]),
  value=[("🔎","Reliable answers","From internal documents."),("🧾","Evidence visible","Every answer can be checked."),("🤝","Trusted by staff","And by customers.")]),

 dict(slug="TN-Farmer-Scheme-AI", icon="🌾", name="TN Farmer Scheme AI", cat="RAG and search",
  promise="Helps Tamil Nadu farmers find the government schemes they qualify for.",
  summary="Farmers ask in English, Tamil or Tanglish, and answers come only from official scheme data.",
  status="Working demo", tech=["Python","Streamlit","BGE embeddings","FAISS","BM25","cross-encoder reranker","Qwen 2.5 (Ollama, runs locally)"],
  links=[("GitHub","https://github.com/Seema777111-git/RAG/tree/main/TN_FARMER_SCHEME_AI")],
  videos=[("Demo · 2 min 23 s", CDN+"RAG@main/TN_FARMER_SCHEME_AI/demo/tn-farmer-scheme-ai-demo.mp4","Real recording of the running app, with narration")],
  problem="Scheme information is spread across government pages written in official language, mostly in English. Many farmers never learn about subsidies that exist for them, or which documents they need.",
  solution=[("Multilingual","English, Tamil and Tanglish"),("Official data only","from the TN Agrisnet portal, with the source cited"),("Hybrid retrieval","meaning-based and keyword search, then reranking"),("Guardrails","refuse off-topic or unclear questions")],
  results_title="Results shown in the demo", stats=[("32","official schemes indexed"),("63","indexed text chunks"),("10/10","labelled evaluation questions passed (English, Tamil, Tanglish)")],
  rag=dict(
   index=[("🏛️","Official data","TN Agrisnet scheme pages"),("✂️","Chunking","32 schemes → 63 chunks"),("🧮","BGE embeddings","Meaning stored as numbers"),("🗂️","Two indexes","FAISS (meaning) + BM25 (keywords)")],
   query=[("🗣️","Farmer asks","English, Tamil or Tanglish"),("🛡️","Guardrail","Refuses off-topic or unclear"),("🔎","Hybrid retrieval","Meaning + keyword search"),("🏅","Reranker","Cross-encoder picks the best"),("✅","Answer + source","Qwen 2.5, runs locally")],
   link=(3,2),
   concepts=[("🔎","Hybrid retrieval","Combines meaning-based search with keyword search, so both phrasing and exact scheme names are found."),("🔤","BM25","A keyword ranking method that rewards exact matches such as scheme names."),("🏅","Reranking","A cross-encoder reads each candidate passage with the question and keeps the most relevant."),("🏠","Local LLM","Qwen 2.5 runs locally through Ollama to write the final answer."),("🛡️","Guardrails","Off-topic or unclear questions are refused instead of guessed."),("🗣️","Multilingual","Questions in English, Tamil or Tanglish reach the same official data.")]),
  value=[("🗣️","In their own language","English, Tamil or Tanglish."),("📚","Official sources","Answers users can verify."),("🔁","Reusable approach","For any large set of rules or product information.")]),

 dict(slug="Voice-AI-Agent", icon="🎙️", name="Voice AI Agent", cat="Voice and automation",
  promise="A Telegram assistant customers can talk to.",
  summary="It listens, finds live information, calculates, sends emails, and replies in text and voice.",
  status="Working demo", tech=["n8n (self-hosted, Docker)","Telegram","OpenAI Whisper","GPT-4o-mini","SerpAPI","Gmail","OpenAI TTS"],
  links=[("GitHub","https://github.com/Seema777111-git/Saki-AI-Portfolio/tree/main/Voice-AI-Agent")],
  videos=[("Demo · 2 min 52 s", CDN+"Saki-AI-Portfolio@main/Voice-AI-Agent/demo/voice-ai-agent-demo.mp4","Real recording of the bot in Telegram Desktop, with narration")],
  problem="Customers increasingly send voice notes instead of typing. Jewellers, clinics and agents receive the same questions all day, often after hours, and cannot reply to every message quickly.",
  solution=[("Understands voice and text","with OpenAI Whisper"),("Uses live data","through Google search (SerpAPI)"),("Calculates reliably","with a calculator tool"),("Takes action","by sending emails through Gmail"),("Replies twice","full text plus a short spoken summary")],
  results_title="Results from the recorded demo", results_table=(["Customer request (spoken)","Outcome"],[["Price of 22 carat gold in Chennai today","<b>₹12,800 per gram</b>, quoted from the search result"],["Cost of 10 grams including GST","<b>₹1,31,840</b> (12,800 × 10 × 1.03), from the calculator tool"],["“Send this to my email”","<b>Email delivered at 2:02 PM</b>; Gmail confirmed it was sent"]]),
  infographic=RAW+"Voice-AI-Agent/images/n8n-workflow.png",
  flow="Telegram → Switch (voice or text) → Whisper → AI Agent (GPT-4o-mini + memory + SerpAPI, Calculator, Gmail) → text reply + spoken summary → OpenAI TTS → voice reply",
  safeguards=["Only quotes a number that appears in the search results; otherwise it says so","Never reports an email as sent unless Gmail confirms it","Replies are escaped so special characters cannot block delivery"],
  value=[("🕒","24×7 answers","No missed enquiries at night or on holidays."),("🧑‍💼","Saves staff time","Repeat questions are handled automatically."),("✅","Takes action","Quotes and summaries by email, not just replies.")],
  suits=(["Business","Example customer question"],[["Jewellery shops","“What is today's 22K rate? Email me a quote for 10 grams.”"],["Clinics","“When is the doctor available on Saturday?”"],["Property agents","“Do you have 2BHK flats near Velachery? Send me the brochure.”"],["Farm-supply dealers","“இன்று உரம் விலை என்ன?” (today's fertiliser price, in Tamil)"]]),
  commercial="A one-time setup fee plus a monthly plan covering hosting, AI usage and support. Optional add-ons: the client's own price list or API, a WhatsApp channel, lead logging to Google Sheets or a CRM, appointment booking, Tamil and Hindi replies, and a daily summary to the owner."),
]

CSS = """
html{scrollbar-width:none;-ms-overflow-style:none}html::-webkit-scrollbar,body::-webkit-scrollbar{display:none;width:0;height:0}
:root{color-scheme:light;--purple:#7137B8;--pink:#D94D9B;--lav:#C6A6F2;--char:#45404B;--muted:#6E6877;--line:#EADFF7;--lav-bg:#F6F0FD;--pink-bg:#FDF2F8;
--shadow:0 6px 22px rgba(113,55,184,.09);--glow:0 12px 32px rgba(217,77,155,.20);--h:"Plus Jakarta Sans",Inter,sans-serif}
*{box-sizing:border-box;margin:0;padding:0}
body{background:#fff;font-family:Inter,"Segoe UI",system-ui,sans-serif;color:var(--char);font-size:14.5px;line-height:1.65;text-align:left}
a{color:inherit}
.sec{padding:44px 48px}.lav{background:var(--lav-bg)}.pink{background:var(--pink-bg)}
.inner{max-width:1000px;margin:0}
.hero{padding:34px 48px 30px;background:linear-gradient(180deg,#FBF8FF,#fff)}
.eyebrow{font-size:11.5px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--pink)}
.promise{font-family:var(--h);font-size:26px;font-weight:800;line-height:1.25;color:var(--purple);letter-spacing:-.01em;margin:8px 0 10px;max-width:820px}
.summary{max-width:780px;font-size:15px}
.meta{display:flex;flex-wrap:wrap;gap:6px;margin-top:16px}
.tag{font-size:12px;font-weight:600;padding:4px 10px;border-radius:999px;background:var(--lav-bg);border:1px solid var(--line);color:var(--purple)}
.tag.ok{background:#EAF6EE;border-color:#CFE8D6;color:#2F7A45}.tag.cat{background:var(--pink-bg);border-color:#F4C3DE;color:var(--pink)}
.btns{display:flex;flex-wrap:wrap;gap:8px;margin-top:18px}
.btn{display:inline-flex;align-items:center;gap:6px;padding:8px 15px;border-radius:999px;font-size:13px;font-weight:600;text-decoration:none;border:1px solid var(--line);background:#fff;transition:transform .2s,box-shadow .2s,border-color .2s}
.btn:hover{transform:translateY(-2px);box-shadow:var(--glow);border-color:var(--pink)}
.btn.primary{background:var(--purple);border-color:var(--purple);color:#fff}
.price{margin-top:12px;font-size:13.5px;font-weight:600;color:var(--pink)}
/* numbered heading, same as the main page (style C) */
.head{position:relative;padding-left:72px;min-height:56px;margin-bottom:22px}
.num{position:absolute;left:0;top:-4px;font-family:var(--h);font-size:46px;font-weight:800;line-height:1;color:var(--lav);opacity:.8}
.h2{font-family:var(--h);font-size:24px;font-weight:700;color:var(--purple);line-height:1.2;letter-spacing:-.01em;margin-top:4px}
.sub{margin-top:6px;font-size:13.5px;color:var(--muted);border-left:2px solid var(--pink);padding-left:10px}
.tabs{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:10px}
.tabs button{border:1px solid var(--line);background:#fff;border-radius:999px;padding:6px 14px;font:600 13px Inter,sans-serif;color:var(--purple);cursor:pointer}
.tabs button.on{background:var(--purple);border-color:var(--purple);color:#fff}
video{width:100%;max-width:960px;border-radius:14px;background:#F6F0FD;display:block;box-shadow:var(--shadow);border:1px solid var(--line)}
.cap{font-size:12.5px;color:var(--muted);margin-top:6px}
.two{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.card{background:#fff;border:1px solid var(--line);border-radius:16px;padding:20px 22px;box-shadow:var(--shadow)}
.card h3{font-family:var(--h);font-size:17px;color:var(--purple);margin-bottom:8px}
.card ul{margin-left:18px}.card li{margin-top:5px}
.card li b,.card p b{color:var(--purple)}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:14px}
.stat{background:#fff;border:1px solid var(--line);border-radius:16px;padding:18px;box-shadow:var(--shadow)}
.stat b{display:block;font-family:var(--h);font-size:28px;color:var(--purple);line-height:1.1}
.stat span{font-size:12.5px;color:var(--muted)}
table{width:100%;border-collapse:separate;border-spacing:0;background:#fff;border:1px solid var(--line);border-radius:14px;overflow:hidden;box-shadow:var(--shadow);font-size:13.5px}
th{background:var(--pink-bg);color:var(--pink);text-align:left;font-size:12px;letter-spacing:.06em;text-transform:uppercase;padding:10px 14px}
td{padding:10px 14px;border-top:1px solid var(--line);vertical-align:top}
td b{color:var(--purple)}
.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;counter-reset:s}
.step{background:#fff;border:1px solid var(--line);border-radius:14px;padding:16px;box-shadow:var(--shadow)}
.step::before{counter-increment:s;content:"0" counter(s);display:block;font-family:var(--h);font-weight:800;font-size:22px;color:var(--lav)}
.step b{color:var(--purple)}.step p{font-size:13px;margin-top:2px}
.shots{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.shots img,.info img{width:100%;border-radius:12px;border:1px solid var(--line);box-shadow:var(--shadow);display:block;background:#fff}
.info{max-width:960px}.info a{display:block}
.flow{margin-top:14px;background:#fff;border:1px solid var(--line);border-left:4px solid var(--pink);border-radius:12px;padding:14px 16px;font-size:13.5px;max-width:960px}
.bul{margin:14px 0 0 18px;max-width:900px}.bul li{margin-top:5px}
.vals{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.val{background:#fff;border:1px solid var(--line);border-radius:16px;padding:18px;box-shadow:var(--shadow);transition:transform .25s,box-shadow .25s}
.val:hover{transform:translateY(-4px);box-shadow:var(--glow)}
.val .i{font-size:24px}.val b{display:block;font-family:var(--h);font-size:16px;color:var(--purple);margin-top:6px}.val span{font-size:13px}
details{margin-top:16px;background:#fff;border:1px solid var(--line);border-radius:12px;padding:12px 16px;max-width:960px}
summary{cursor:pointer;font-family:var(--h);font-weight:700;color:var(--purple)}
details p{margin-top:8px;font-size:13.5px}
.foot{padding:26px 48px 34px;border-top:1px solid var(--line)}
.foot p{font-size:12.5px;color:var(--muted)}
.foot .btns{margin-top:12px}
.rag{background:#fff;border:1px solid var(--line);border-radius:16px;padding:18px 18px 8px;box-shadow:var(--shadow);max-width:1000px}
.rag svg{width:100%;height:auto;display:block}
.cons{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:16px;max-width:1000px}
.con{background:#fff;border:1px solid var(--line);border-radius:14px;padding:14px 16px;box-shadow:var(--shadow)}
.con b{display:block;font-family:var(--h);color:var(--purple);font-size:14.5px;margin:2px 0 3px}.con span{font-size:12.8px}
.minih{font-family:var(--h);font-size:16px;color:var(--purple);margin:22px 0 0}
@media (max-width:640px){.cons{grid-template-columns:1fr}}
.reveal{opacity:0;transform:translateY(14px);transition:opacity .6s ease,transform .6s ease}.reveal.in{opacity:1;transform:none}
@media (prefers-reduced-motion:reduce){.reveal{opacity:1;transform:none}}
@media (max-width:640px){.sec,.hero,.foot{padding-left:18px;padding-right:18px}.two,.vals,.shots,.steps{grid-template-columns:1fr}
 .head{padding-left:52px}.num{font-size:34px}.h2{font-size:20px}.promise{font-size:21px}}
"""

def _wrap(t, n):
    out, cur = [], ""
    for w in t.split():
        if len((cur + " " + w).strip()) <= n: cur = (cur + " " + w).strip()
        else: out.append(cur); cur = w
    out.append(cur); return out

def rag_svg(r):
    W, PAD, GAP = 960, 8, 26
    def row(items, y, label, color):
        n = len(items); bw = (W - 2 * PAD - GAP * (n - 1)) / n; parts = []; centers = []
        parts.append(f'<text x="{PAD}" y="{y-14}" font-size="12.5" font-weight="700" letter-spacing="1.6" fill="{color}">{E(label)}</text>')
        for i, (ic, t, d) in enumerate(items):
            x = PAD + i * (bw + GAP); cx = x + bw / 2; centers.append((cx, x, bw))
            parts.append(f'<rect x="{x:.1f}" y="{y}" width="{bw:.1f}" height="124" rx="14" fill="#fff" stroke="#E2D2F8" stroke-width="1.5"/>')
            parts.append(f'<circle cx="{cx:.1f}" cy="{y+30}" r="19" fill="#F3EBFD" stroke="#C6A6F2"/><text x="{cx:.1f}" y="{y+37}" font-size="19" text-anchor="middle">{ic}</text>')
            parts.append(f'<text x="{cx:.1f}" y="{y+70}" font-size="14" font-weight="700" fill="#7137B8" text-anchor="middle" font-family="Plus Jakarta Sans,Inter,sans-serif">{E(t)}</text>')
            for k, ln in enumerate(_wrap(d, int(bw / 7.2))[:3]):
                parts.append(f'<text x="{cx:.1f}" y="{y+90+k*15}" font-size="11.5" fill="#45404B" text-anchor="middle">{E(ln)}</text>')
            if i < n - 1:
                ax = x + bw + 3
                parts.append(f'<path d="M{ax:.1f} {y+62} h{GAP-10}" stroke="#D94D9B" stroke-width="2.5" fill="none" marker-end="url(#ar)"/>')
        return parts, centers
    p1, c1 = row(r["index"], 34, "1 · INDEXING · done once", "#D94D9B")
    p2, c2 = row(r["query"], 240, "2 · ANSWERING · every question", "#7137B8")
    a, b = r["link"]; x1 = c1[a][0]; x2 = c2[b][0]
    link = (f'<path d="M{x1:.1f} 160 C {x1:.1f} 200, {x2:.1f} 190, {x2:.1f} 236" stroke="#7137B8" stroke-width="2" stroke-dasharray="6 5" fill="none" marker-end="url(#ar2)"/>'
            f'<text x="{(x1+x2)/2+8:.1f}" y="201" font-size="11.5" font-weight="600" fill="#7137B8">retrieves evidence</text>')
    defs = ('<defs><marker id="ar" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="#D94D9B"/></marker>'
            '<marker id="ar2" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="#7137B8"/></marker></defs>')
    return f'<div class="rag"><svg viewBox="0 0 {W} 380" role="img" aria-label="How retrieval-augmented generation works in this project" font-family="Inter,Segoe UI,sans-serif">{defs}{"".join(p1)}{link}{"".join(p2)}</svg></div>'

def concepts_html(cs):
    return '<h3 class="minih">Key RAG concepts</h3><div class="cons">' + "".join(f'<div class="con"><span>{i}</span><b>{E(t)}</b><span>{E(d)}</span></div>' for i, t, d in cs) + "</div>"

def section(n, title, body, sub="", bg=""):
    s = f'<p class="sub">{sub}</p>' if sub else ""
    return f'<section class="sec {bg}"><div class="inner reveal"><div class="head"><span class="num">{n:02d}</span><span class="eyebrow">{E(title[0])}</span><h2 class="h2">{E(title[1])}</h2>{s}</div>{body}</div></section>'

def table(head, rows):
    return "<table><tr>" + "".join(f"<th>{E(h)}</th>" for h in head) + "</tr>" + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</table>"

def build(p):
    tags = f'<span class="tag ok">✅ {E(p["status"])}</span><span class="tag cat">{E(p["cat"])}</span>' + "".join(f'<span class="tag">{E(t)}</span>' for t in p["tech"])
    btns = "".join(f'<a class="btn{" primary" if i == 0 else ""}" href="{u}" target="_blank" rel="noopener">{E(t)}</a>' for i, (t, u) in enumerate(p.get("links", [])))
    price = f'<p class="price">💰 {E(p["price"])}</p>' if p.get("price") else ""
    hero = f'<header class="hero"><div class="inner reveal"><span class="eyebrow">{p["icon"]} {E(p["cat"])}</span><h1 class="promise">{E(p["promise"])}</h1><p class="summary">{E(p["summary"])}</p><div class="meta">{tags}</div>{price}{f"<div class=btns>{btns}</div>" if btns else ""}</div></header>'
    out, n = [hero], 0
    vids = p["videos"]
    if len(vids) > 1:
        tabs = "".join(f'<button class="{"on" if i == 0 else ""}" data-i="{i}">{E(t)}</button>' for i, (t, _, _) in enumerate(vids))
        vb = f'<div class="tabs">{tabs}</div><video id="v" controls preload="metadata" playsinline src="{vids[0][1]}"></video><p class="cap" id="vc">{E(vids[0][2])}</p><script>const V={[ [u, c] for _, u, c in vids ]!r};document.querySelectorAll(".tabs button").forEach(b=>b.onclick=()=>{{document.querySelectorAll(".tabs button").forEach(x=>x.classList.remove("on"));b.classList.add("on");const [u,c]=V[b.dataset.i];const v=document.getElementById("v");v.src=u;document.getElementById("vc").textContent=c}})</script>'
        title = ("Demo", "Watch it working")
    else:
        vb = f'<video controls preload="metadata" playsinline src="{vids[0][1]}"></video><p class="cap">{E(vids[0][2])}</p>'
        title = ("Demo", vids[0][0].replace("Demo", "Watch it working"))
    n += 1; out.append(section(n, title, vb, bg="lav"))
    sol = "".join(f"<li><b>{E(a)}</b>: {E(b)}</li>" for a, b in p["solution"])
    n += 1; out.append(section(n, ("Problem and solution", "The business problem, solved"),
        f'<div class="two"><div class="card"><h3>🎯 The problem</h3><p>{p["problem"]}</p></div><div class="card"><h3>💡 The solution</h3><ul>{sol}</ul></div></div>'))
    if p.get("stats"):
        b = '<div class="stats">' + "".join(f"<div class=stat><b>{E(a)}</b><span>{E(c)}</span></div>" for a, c in p["stats"]) + "</div>"
        n += 1; out.append(section(n, ("Proof", p["results_title"]), b, bg="pink"))
    elif p.get("results_table"):
        n += 1; out.append(section(n, ("Proof", p["results_title"]), table(*p["results_table"]), bg="pink"))
    elif p.get("steps"):
        b = '<div class="steps">' + "".join(f"<div class=step><b>{E(a)}</b><p>{E(c)}</p></div>" for a, c in p["steps"]) + "</div>"
        n += 1; out.append(section(n, ("Journey", p["results_title"]), b, bg="pink"))
    if p.get("screens"):
        b = '<div class="shots">' + "".join(f'<a href="{u}" target="_blank" rel="noopener"><img src="{u}" alt="Screen {i+1}" loading="lazy"></a>' for i, u in enumerate(p["screens"])) + "</div>"
        n += 1; out.append(section(n, ("Screens", "Inside the app"), b, bg="pink"))
    hw = ""
    if p.get("rag"): hw += f'<div class="info"><a href="{RAW}{p["slug"]}/images/how-it-works.jpg" target="_blank" rel="noopener"><img src="{RAW}{p["slug"]}/images/how-it-works.jpg" alt="How RAG works in {E(p["name"])}" loading="lazy"></a></div>' + concepts_html(p["rag"]["concepts"])
    if p.get("infographic"): hw += f'<div class="info"><a href="{p["infographic"]}" target="_blank" rel="noopener"><img src="{p["infographic"]}" alt="{E(p["name"])} infographic" loading="lazy"></a></div>'
    if p.get("flow"): hw += f'<div class="flow">🔄 {E(p["flow"])}</div>'
    if p.get("how"): hw += '<ul class="bul">' + "".join(f"<li>{h}</li>" for h in p["how"]) + "</ul>"
    if hw:
        n += 1; out.append(section(n, ("How it works", "Under the hood"), hw, sub=("How RAG (retrieval-augmented generation) works here: the AI answers only from evidence it retrieves." if p.get("rag") else ("Click the picture to open it full size." if p.get("infographic") else ""))))
    if p.get("safeguards"):
        n += 1; out.append(section(n, ("Responsible AI", "Reliability safeguards"), '<div class="card"><ul>' + "".join(f"<li>{E(s)}</li>" for s in p["safeguards"]) + "</ul></div>", bg="lav"))
    vb = '<div class="vals">' + "".join(f'<div class="val"><span class="i">{i}</span><b>{E(a)}</b><span>{E(c)}</span></div>' for i, a, c in p["value"]) + "</div>"
    if p.get("suits"): vb += '<div style="margin-top:16px">' + table(*p["suits"]) + "</div>"
    if p.get("commercial"): vb += f'<details><summary>💰 Commercial model</summary><p>{E(p["commercial"])}</p></details>'
    n += 1; out.append(section(n, ("Business value", "Why it matters"), vb, bg="pink"))
    note = f'<p>{E(p["note"])}</p>' if p.get("note") else ""
    out.append(f'<footer class="foot">{note}<div class="btns"><a class="btn" href="{HOME}" target="_top">← Back to portfolio</a><a class="btn primary" href="mailto:saki777111@gmail.com">📧 saki777111@gmail.com</a></div></footer>')
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="color-scheme" content="light">
<title>{E(p["name"])} · Case Study</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@700;800&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>
{''.join(out)}
<script>const io=new IntersectionObserver(es=>es.forEach(e=>{{if(e.isIntersecting){{e.target.classList.add("in");io.unobserve(e.target)}}}}),{{threshold:.08}});document.querySelectorAll(".reveal").forEach(el=>io.observe(el));
const tell=()=>{{const f=document.querySelector(".foot");const h=Math.ceil(f.getBoundingClientRect().bottom+scrollY);parent.postMessage({{caseHeight:h}},"*")}};addEventListener("load",tell);addEventListener("resize",tell);new ResizeObserver(tell).observe(document.body);setTimeout(tell,800);setTimeout(tell,2500);</script>
</body></html>"""

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for p in PROJECTS:
        open(os.path.join(OUT, p["slug"] + ".html"), "w", encoding="utf-8").write(build(p))
    print("built", len(PROJECTS))
