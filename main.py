import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse, HTMLResponse
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.middleware.trustedhost import TrustedHostMiddleware
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from api.routers.client_router import router as client_router

app = FastAPI(
    title="Tadjic entertainment limited corporation"
)

app.include_router(client_router)


app.add_middleware(
    TrustedHostMiddleware, allowed_hosts=["*"]
)


@app.get("/")
def root(request: Request):
    return RedirectResponse(url='/mainPage')


app.mount("/static_main_page", StaticFiles(directory="frontend/main_page"), name="mainPage")
app.mount("/static_check_status_order_page", StaticFiles(directory="frontend/check_status_order_page"), name="checkOrderStatus")
app.mount("/static_404_errorPage", StaticFiles(directory="frontend/404_errorPage"), name="404")

templates = Jinja2Templates(directory="frontend")


class NotFoundMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ):
        response = await call_next(request)
        if response.status_code == 404:
            return templates.TemplateResponse("404_errorPage/404.html", {"request": request}, status_code=404)
        return response


app.add_middleware(NotFoundMiddleware)


@app.get("/404", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("404_errorPage/404.html", {"request": request})


@app.get("/mainPage", response_class=HTMLResponse)
async def get_home_page(request: Request):
    return templates.TemplateResponse("main_page/mainPage.html", {"request": request})


@app.get("/checkOrderStatus", response_class=HTMLResponse)
async def get_home_page(request: Request):
    return templates.TemplateResponse("check_status_order_page/checkOrderStatus.html", {"request": request})


if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)
