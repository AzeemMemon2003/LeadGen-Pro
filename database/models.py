LEADS_TABLE = """

CREATE TABLE IF NOT EXISTS leads (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    company TEXT,

    website TEXT UNIQUE,

    primary_email TEXT,

    backup_emails TEXT,

    phone TEXT,

    address TEXT,

    technology TEXT,

    score INTEGER,

    priority TEXT,

    status TEXT,

    source TEXT,

    contact_form TEXT,

    whatsapp TEXT,

    linkedin TEXT,

    website_score INTEGER,

    website_strengths TEXT,

    website_weaknesses TEXT,

    website_opportunities TEXT,

    created_at TEXT,

    updated_at TEXT

)

"""