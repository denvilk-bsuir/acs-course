from datetime import datetime
from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import plotly.express as px
from api.v1.api import app as app_v1
from core import dependencies

app = FastAPI()

origins = [
    # 'http://localhost:5173',
    # 'localhost:5173',
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.mount('/v1', app_v1)

@app.get('/ping')
async def ping():
    return {'message':'pong'}

@app.get("/")
async def dashboard(service = Depends(dependencies.stats_service)):
    result = await service.get_stats_from_time()
    res = {}
    for item in result:
        d: datetime = item.created_at
        r = datetime(year=d.year, month=d.month, day=d.day, hour=d.hour, minute=d.minute, second=d.second, tzinfo=d.tzinfo)
        res[r] = res.get(r, 0) + 1
    x = res.keys()
    y = res.values()
    plot = px.line(x=sorted(x), y=[res[t] for t in sorted(x)], title="Last 1 hour queries",labels={'x':'Date', 'y':"Count"})
    t = "\n".join([f"<tr><td>{item.destination}</td><td>{item.count}</td></tr>" for item in (await service.get_stats_top_100())])
    html = f"""
<!doctype html>
<html>
<head>
    <title>Dashboard</title>
</head>
<body style="display: flex; justify-content: center; flex-direction: column;">
{plot.to_html()}
<table style="border: 1px solid black;">
<tr><th colspan="2">Top 20 destinations for last 10 min</th></tr>
{t}
</table>
</body>
</html>
"""
    return HTMLResponse(content=html, status_code=200)