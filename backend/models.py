"""
Database Models - ÙÙØ§Ø°Ø¬ ÙØ§Ø¹Ø¯Ø© Ø§ÙØ¨ÙØ§ÙØ§Øª
"""
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, Text, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

Base = declarative_base()


# âââââââââââââââââââââââââââââââââââââââââââ
# SQLAlchemy Models (Database Tables)
# âââââââââââââââââââââââââââââââââââââââââââ

class CarListing(Base):
    """Ø¬Ø¯ÙÙ Ø§ÙØ³ÙØ§Ø±Ø§Øª Ø§ÙÙØ¹Ø±ÙØ¶Ø©"""
    __tablename__ = "car_listings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    source = Column(String(50), nullable=False)  # manheim, copart, iaai, cars.com
    source_id = Column(String(100))  # ID ÙÙ Ø§ÙÙÙÙØ¹ Ø§ÙØ£ØµÙÙ
    source_url = Column(Text)

    # ÙØ¹ÙÙÙØ§Øª Ø§ÙØ³ÙØ§Ø±Ø© Ø§ÙØ£Ø³Ø§Ø³ÙØ©
    year = Column(Integer)
    make = Column(String(100))  # Ø§ÙØ´Ø±ÙØ© Ø§ÙÙØµÙØ¹Ø©
    model = Column(String(100))  # Ø§ÙÙÙØ¯ÙÙ
    trim = Column(String(100))  # Ø§ÙÙØ¦Ø©
    vin = Column(String(17))  # Ø±ÙÙ Ø§ÙÙÙÙÙ

    # Ø§ÙØªÙØ§ØµÙÙ
    mileage = Column(Integer)  # Ø§ÙÙÙÙÙÙØªØ±Ø§Øª
    color = Column(String(50))
    interior_color = Column(String(50))
    fuel_type = Column(String(50))  # Ø¨ÙØ²ÙÙØ Ø¯ÙØ²ÙØ ÙÙØ±Ø¨Ø§Ø¦ÙØ ÙØ§ÙØ¨Ø±Ø¯
    transmission = Column(String(50))  # Ø£ÙØªÙÙØ§ØªÙÙØ Ø¹Ø§Ø¯Ù
    engine = Column(String(100))
    drivetrain = Column(String(50))  # Ø¯ÙØ¹ Ø£ÙØ§ÙÙØ Ø®ÙÙÙØ Ø±Ø¨Ø§Ø¹Ù
    body_type = Column(String(50))  # Ø³ÙØ¯Ø§ÙØ SUVØ Ø¨ÙÙ Ø£Ø¨...
    condition = Column(String(50))  # Ø§ÙØ­Ø§ÙØ©
    condition_grade = Column(Float)  # ØªÙÙÙÙ Ø§ÙØ­Ø§ÙØ© ÙÙ 1-5

    # Ø§ÙØ£Ø³Ø¹Ø§Ø±
    price = Column(Float)  # Ø§ÙØ³Ø¹Ø± Ø§ÙØ­Ø§ÙÙ
    market_value = Column(Float)  # Ø§ÙÙÙÙØ© Ø§ÙØ³ÙÙÙØ© (MMR Ø£Ù KBB)
    deal_score = Column(Float)  # ÙÙØ§Ø· Ø§ÙØµÙÙØ© (ÙÙÙØ§ ÙØ§ÙØª Ø£Ø¹ÙÙ ÙØ§ÙØª Ø§ÙØµÙÙØ© Ø£ÙØ¶Ù)
    savings = Column(Float)  # Ø§ÙØªÙÙÙØ± Ø§ÙÙÙØ¯Ø±

    # Ø§ÙØµÙØ±
    images = Column(JSON)  # ÙØ§Ø¦ÙØ© Ø±ÙØ§Ø¨Ø· Ø§ÙØµÙØ±
    thumbnail = Column(Text)

    # Ø§ÙÙÙÙØ¹
    location = Column(String(200))
    latitude = Column(Float)
    longitude = Column(Float)

    # ÙØ¹ÙÙÙØ§Øª Ø§ÙÙØ²Ø§Ø¯
    auction_date = Column(DateTime)
    auction_type = Column(String(50))  # online, in-lane
    bid_count = Column(Integer, default=0)

    # Ø§ÙØªÙØ§Ø±ÙØ®
    scraped_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    is_active = Column(Boolean, default=True)


class PriceHistory(Base):
    """Ø¬Ø¯ÙÙ ØªØ§Ø±ÙØ® Ø§ÙØ£Ø³Ø¹Ø§Ø±"""
    __tablename__ = "price_history"

    id = Column(Integer, primary_key=True, autoincrement=True)
    car_listing_id = Column(Integer)
    price = Column(Float)
    recorded_at = Column(DateTime, default=func.now())


class UserAlert(Base):
    """Ø¬Ø¯ÙÙ ØªÙØ¨ÙÙØ§Øª Ø§ÙÙØ³ØªØ®Ø¯Ù"""
    __tablename__ = "user_alerts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255))
    make = Column(String(100))
    model = Column(String(100))
    year_min = Column(Integer)
    year_max = Column(Integer)
    price_max = Column(Float)
    mileage_max = Column(Integer)
    min_deal_score = Column(Float, default=70)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())


# âââââââââââââââââââââââââââââââââââââââââââ
# Pydantic Models (API Schemas)
# âââââââââââââââââââââââââââââââââââââââââââ

class CarListingResponse(BaseModel):
    id: int
    source: str
    year: Optional[int] = None
    make: Optional[str] = None
    model: Optional[str] = None
    trim: Optional[str] = None
    vin: Optional[str] = None
    mileage: Optional[int] = None
    color: Optional[str] = None
    fuel_type: Optional[str] = None
    transmission: Optional[str] = None
    body_type: Optional[str] = None
    condition: Optional[str] = None
    condition_grade: Optional[float] = None
    price: Optional[float] = None
    market_value: Optional[float] = None
    deal_score: Optional[float] = None
    savings: Optional[float] = None
    thumbnail: Optional[str] = None
    images: Optional[list] = None
    location: Optional[str] = None
    auction_date: Optional[datetime] = None
    source_url: Optional[str] = None
    scraped_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class SearchFilters(BaseModel):
    make: Optional[str] = None
    model: Optional[str] = None
    year_min: Optional[int] = None
    year_max: Optional[int] = None
    price_min: Optional[float] = None
    price_max: Optional[float] = None
    mileage_max: Optional[int] = None
    body_type: Optional[str] = None
    fuel_type: Optional[str] = None
    transmission: Optional[str] = None
    source: Optional[str] = None  # manheim, copart, iaai, cars.com
    sort_by: str = Field(default="deal_score")  # deal_score, price, mileage, year
    sort_order: str = Field(default="desc")
    page: int = Field(default=1, ge=1)
    per_page: int = Field(default=20, ge=1, le=100)


class AlertCreate(BaseModel):
    email: str
    make: Optional[str] = None
    model: Optional[str] = None
    year_min: Optional[int] = None
    year_max: Optional[int] = None
    price_max: Optional[float] = None
    mileage_max: Optional[int] = None
    min_deal_score: float = Field(default=70)


class DashboardStats(BaseModel):
    total_listings: int
    avg_deal_score: float
    best_deal: Optional[CarListingResponse] = None
    total_savings: float
    listings_by_source: dict
    top_makes: dict
    price_distribution: list
    recent_deals: List[CarListingResponse]
