from fastapi import APIRouter, Query, Depends

from app import dto
from app.api import schems
from app.api.dependencies import get_user

router = APIRouter(prefix="/link")


@router.get(
    path="/all",
    description="Get all user links",
    response_model=list[dto.Link]
)
async def get_user_links(
        page: int = Query(default=1),
        limit: int = Query(default=10),
        user: dto.User = Depends(get_user)
) -> list[dto.Link]:
    return [
        dto.Link(
            title="Some title",
            long_url="some",
            short_url="some",
            clicks=0
        ),
        dto.Link(
            title="Some title",
            long_url="some",
            short_url="some",
            clicks=0
        )
    ]


@router.post(
    path="/new",
    description="Short a new link",
    response_model=dto.ShortUrl
)
async def short_link(
        link: schems.ShortUrl
) -> dto.ShortUrl:
    return dto.ShortUrl(title="New link", short_url="short_url", long_url="long_url")
