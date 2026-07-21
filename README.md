# Maximum Wash — Recontact

A customer re-engagement dashboard built from the 2024 ServiceM8 completed-jobs
master sheet. It splits previous customers between the two salespeople, ranks
them by value and time since last service, tracks outreach progress, and drafts
personalised follow-up emails.

## The lists

Assignment comes from the row highlight colour in the master sheet
(green = Bas, red = Herman, no colour = Herman; a customer with jobs in more
than one colour goes green-first):

| Owner | Customers | 2024 revenue |
|---|---|---|
| Bas (green) | 114 | $1,882,278 |
| Herman (red + uncoloured) | 348 | $1,175,448 |
| **Total** | **462** | **$3,056,876** |

Jobs are grouped per customer by email address, so repeat customers appear
once with their full 2024 job history.

## Using the dashboard

Open `dist/index.html` (or the published artifact link). On first open, pick
your name — the view opens on your list and email drafts are signed as you.

- **Filter** by owner, client type, outreach status, or free-text search.
- **Sort** by 2024 value, longest-since-job, most recent, job count, or name.
- **"Time since last job"** strip: click a bar to focus a recency band.
  12+ months is the warm re-wash window.
- **Click a customer** for contact details, job history, status + notes,
  and a pre-written outreach email (copy it, or open in your mail app).

### Progress sync (important)

The page is a static file, so status and notes save **per device**
(browser localStorage) — Bas and Herman each see their own edits only.
To sync: **Export progress** on one device, send the file over, and
**Import / merge** on the other (newest update per customer wins).
For live shared tracking, the next step is hosting this as a small web app
with a database — the code here is the foundation for that.

## Rebuilding from a fresh export

```bash
python3 scripts/extract_customers.py "<ServiceM8 export>.xlsx" data/customers.json
python3 scripts/build.py
```

`scripts/extract_customers.py` reads the "Jan-Dec 2024" sheet, reads the row
colours for assignment, and derives "last serviced" from the latest
`Scheduled for … on d/m/yyyy` date in the Booking column (the booking history
runs into 2025–26, which is the honest recency signal — many 2024 customers
were re-serviced later).

## Layout

- `dashboard/template.html` — the dashboard UI (data injected at build time)
- `data/customers.json` — extracted customer list (contains customer PII —
  keep this repo private)
- `scripts/` — extraction + build
- `dist/index.html` — built, self-contained dashboard
