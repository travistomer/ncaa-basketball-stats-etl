from datetime import datetime
from typing import List, Any
from enum import Enum

class Day:
    date: datetime

    def __init__(self, date: datetime) -> None:
        self.date = date

class Broadcast:
    market: str
    names: List[str]

    def __init__(self, market: str, names: List[str]) -> None:
        self.market = market
        self.names = names

class CuratedRank:
    current: int

    def __init__(self, current: int) -> None:
        self.current = current

class Rel(Enum):
    ATHLETE = "athlete"
    DESKTOP = "desktop"
    PLAYERCARD = "playercard"

class AthleteLink:
    rel: List[Rel]
    href: str

    def __init__(self, rel: List[Rel], href: str) -> None:
        self.rel = rel
        self.href = href

class Position:
    abbreviation: str

    def __init__(self, abbreviation: str) -> None:
        self.abbreviation = abbreviation

class TeamClass:
    id: int

    def __init__(self, id: int) -> None:
        self.id = id

class Athlete:
    id: int
    full_name: str
    display_name: str
    short_name: str
    links: List[AthleteLink]
    headshot: str
    jersey: int
    position: Position
    team: TeamClass
    active: bool

    def __init__(self, id: int, full_name: str, display_name: str, short_name: str, links: List[AthleteLink], headshot: str, jersey: int, position: Position, team: TeamClass, active: bool) -> None:
        self.id = id
        self.full_name = full_name
        self.display_name = display_name
        self.short_name = short_name
        self.links = links
        self.headshot = headshot
        self.jersey = jersey
        self.position = position
        self.team = team
        self.active = active

class LeaderLeader:
    display_value: str
    value: float
    athlete: Athlete
    team: TeamClass

    def __init__(self, display_value: str, value: float, athlete: Athlete, team: TeamClass) -> None:
        self.display_value = display_value
        self.value = value
        self.athlete = athlete
        self.team = team

class CompetitorLeader:
    name: str
    display_name: str
    short_display_name: str
    abbreviation: str
    leaders: List[LeaderLeader]

    def __init__(self, name: str, display_name: str, short_display_name: str, abbreviation: str, leaders: List[LeaderLeader]) -> None:
        self.name = name
        self.display_name = display_name
        self.short_display_name = short_display_name
        self.abbreviation = abbreviation
        self.leaders = leaders

class Record:
    name: str
    abbreviation: str
    type: str
    summary: str

    def __init__(self, name: str, abbreviation: str, type: str, summary: str) -> None:
        self.name = name
        self.abbreviation = abbreviation
        self.type = type
        self.summary = summary

class Statistic:
    name: str
    abbreviation: str
    display_value: str
    rank_display_value: str

    def __init__(self, name: str, abbreviation: str, display_value: str, rank_display_value: str) -> None:
        self.name = name
        self.abbreviation = abbreviation
        self.display_value = display_value
        self.rank_display_value = rank_display_value

class TeamLink:
    rel: List[str]
    href: str
    text: str
    is_external: bool
    is_premium: bool

    def __init__(self, rel: List[str], href: str, text: str, is_external: bool, is_premium: bool) -> None:
        self.rel = rel
        self.href = href
        self.text = text
        self.is_external = is_external
        self.is_premium = is_premium

class CompetitorTeam:
    id: int
    uid: str
    location: str
    name: str
    abbreviation: str
    display_name: str
    short_display_name: str
    color: str
    alternate_color: str
    is_active: bool
    venue: TeamClass
    links: List[TeamLink]
    logo: str
    conference_id: int

    def __init__(self, id: int, uid: str, location: str, name: str, abbreviation: str, display_name: str, short_display_name: str, color: str, alternate_color: str, is_active: bool, venue: TeamClass, links: List[TeamLink], logo: str, conference_id: int) -> None:
        self.id = id
        self.uid = uid
        self.location = location
        self.name = name
        self.abbreviation = abbreviation
        self.display_name = display_name
        self.short_display_name = short_display_name
        self.color = color
        self.alternate_color = alternate_color
        self.is_active = is_active
        self.venue = venue
        self.links = links
        self.logo = logo
        self.conference_id = conference_id

class Competitor:
    id: int
    uid: str
    type: str
    order: int
    home_away: str
    team: CompetitorTeam
    score: int
    curated_rank: CuratedRank
    statistics: List[Statistic]
    records: List[Record]
    leaders: List[CompetitorLeader]

    def __init__(self, id: int, uid: str, type: str, order: int, home_away: str, team: CompetitorTeam, score: int, curated_rank: CuratedRank, statistics: List[Statistic], records: List[Record], leaders: List[CompetitorLeader]) -> None:
        self.id = id
        self.uid = uid
        self.type = type
        self.order = order
        self.home_away = home_away
        self.team = team
        self.score = score
        self.curated_rank = curated_rank
        self.statistics = statistics
        self.records = records
        self.leaders = leaders

class Regulation:
    periods: int

    def __init__(self, periods: int) -> None:
        self.periods = periods

class Format:
    regulation: Regulation

    def __init__(self, regulation: Regulation) -> None:
        self.regulation = regulation

class Market:
    id: int
    type: str

    def __init__(self, id: int, type: str) -> None:
        self.id = id
        self.type = type

class Media:
    short_name: str

    def __init__(self, short_name: str) -> None:
        self.short_name = short_name

class GeoBroadcastType:
    id: int
    short_name: str

    def __init__(self, id: int, short_name: str) -> None:
        self.id = id
        self.short_name = short_name

class GeoBroadcast:
    type: GeoBroadcastType
    market: Market
    media: Media
    lang: str
    region: str

    def __init__(self, type: GeoBroadcastType, market: Market, media: Media, lang: str, region: str) -> None:
        self.type = type
        self.market = market
        self.media = media
        self.lang = lang
        self.region = region

class Groups:
    id: int
    name: str
    short_name: str
    is_conference: bool

    def __init__(self, id: int, name: str, short_name: str, is_conference: bool) -> None:
        self.id = id
        self.name = name
        self.short_name = short_name
        self.is_conference = is_conference

class AwayTeamOddsTeam:
    id: int
    abbreviation: str
    display_name: str
    short_display_name: str

    def __init__(self, id: int, abbreviation: str, display_name: str, short_display_name: str) -> None:
        self.id = id
        self.abbreviation = abbreviation
        self.display_name = display_name
        self.short_display_name = short_display_name

class TeamOdds:
    favorite: bool
    underdog: bool
    team: AwayTeamOddsTeam

    def __init__(self, favorite: bool, underdog: bool, team: AwayTeamOddsTeam) -> None:
        self.favorite = favorite
        self.underdog = underdog
        self.team = team

class Over:
    value: float
    display_value: str
    alternate_display_value: int

    def __init__(self, value: float, display_value: str, alternate_display_value: int) -> None:
        self.value = value
        self.display_value = display_value
        self.alternate_display_value = alternate_display_value

class Total:
    alternate_display_value: str

    def __init__(self, alternate_display_value: str) -> None:
        self.alternate_display_value = alternate_display_value

class Current:
    over: Over
    under: Over
    total: Total

    def __init__(self, over: Over, under: Over, total: Total) -> None:
        self.over = over
        self.under = under
        self.total = total

class Provider:
    id: int
    name: str
    priority: int

    def __init__(self, id: int, name: str, priority: int) -> None:
        self.id = id
        self.name = name
        self.priority = priority

class Odd:
    provider: Provider
    details: str
    over_under: float
    spread: float
    away_team_odds: TeamOdds
    home_team_odds: TeamOdds
    open: Current
    current: Current

    def __init__(self, provider: Provider, details: str, over_under: float, spread: float, away_team_odds: TeamOdds, home_team_odds: TeamOdds, open: Current, current: Current) -> None:
        self.provider = provider
        self.details = details
        self.over_under = over_under
        self.spread = spread
        self.away_team_odds = away_team_odds
        self.home_team_odds = home_team_odds
        self.open = open
        self.current = current

class StatusType:
    id: int
    name: str
    state: str
    completed: bool
    description: str
    detail: str
    short_detail: str

    def __init__(self, id: int, name: str, state: str, completed: bool, description: str, detail: str, short_detail: str) -> None:
        self.id = id
        self.name = name
        self.state = state
        self.completed = completed
        self.description = description
        self.detail = detail
        self.short_detail = short_detail


class Status:
    clock: float
    display_clock: str
    period: int
    type: StatusType

    def __init__(self, clock: float, display_clock: str, period: int, type: StatusType) -> None:
        self.clock = clock
        self.display_clock = display_clock
        self.period = period
        self.type = type

class TicketLink:
    href: str

    def __init__(self, href: str) -> None:
        self.href = href

class Ticket:
    summary: str
    number_available: int
    links: List[TicketLink]

    def __init__(self, summary: str, number_available: int, links: List[TicketLink]) -> None:
        self.summary = summary
        self.number_available = number_available
        self.links = links

class CompetitionType:
    id: int
    abbreviation: str

    def __init__(self, id: int, abbreviation: str) -> None:
        self.id = id
        self.abbreviation = abbreviation

class Address:
    city: str
    state: str

    def __init__(self, city: str, state: str) -> None:
        self.city = city
        self.state = state

class CompetitionVenue:
    id: int
    full_name: str
    address: Address
    capacity: int
    indoor: bool

    def __init__(self, id: int, full_name: str, address: Address, capacity: int, indoor: bool) -> None:
        self.id = id
        self.full_name = full_name
        self.address = address
        self.capacity = capacity
        self.indoor = indoor

class Competition:
    id: int
    uid: str
    date: str
    attendance: int
    type: CompetitionType
    time_valid: bool
    neutral_site: bool
    conference_competition: bool
    play_by_play_available: bool
    recent: bool
    venue: CompetitionVenue
    competitors: List[Competitor]
    notes: List[Any]
    status: Status
    broadcasts: List[Broadcast]
    groups: Groups
    format: Format
    tickets: List[Ticket]
    start_date: str
    geo_broadcasts: List[GeoBroadcast]
    odds: List[Odd]

    def __init__(self, id: int, uid: str, date: str, attendance: int, type: CompetitionType, time_valid: bool, neutral_site: bool, conference_competition: bool, play_by_play_available: bool, recent: bool, venue: CompetitionVenue, competitors: List[Competitor], notes: List[Any], status: Status, broadcasts: List[Broadcast], groups: Groups, format: Format, tickets: List[Ticket], start_date: str, geo_broadcasts: List[GeoBroadcast], odds: List[Odd]) -> None:
        self.id = id
        self.uid = uid
        self.date = date
        self.attendance = attendance
        self.type = type
        self.time_valid = time_valid
        self.neutral_site = neutral_site
        self.conference_competition = conference_competition
        self.play_by_play_available = play_by_play_available
        self.recent = recent
        self.venue = venue
        self.competitors = competitors
        self.notes = notes
        self.status = status
        self.broadcasts = broadcasts
        self.groups = groups
        self.format = format
        self.tickets = tickets
        self.start_date = start_date
        self.geo_broadcasts = geo_broadcasts
        self.odds = odds

class EventLink:
    language: str
    rel: List[str]
    href: str
    text: str
    short_text: str
    is_external: bool
    is_premium: bool

    def __init__(self, language: str, rel: List[str], href: str, text: str, short_text: str, is_external: bool, is_premium: bool) -> None:
        self.language = language
        self.rel = rel
        self.href = href
        self.text = text
        self.short_text = short_text
        self.is_external = is_external
        self.is_premium = is_premium

class EventSeason:
    year: int
    type: int
    slug: str

    def __init__(self, year: int, type: int, slug: str) -> None:
        self.year = year
        self.type = type
        self.slug = slug

class Event:
    id: int
    uid: str
    date: str
    name: str
    short_name: str
    season: EventSeason
    competitions: List[Competition]
    links: List[EventLink]
    status: Status

    def __init__(self, id: int, uid: str, date: str, name: str, short_name: str, season: EventSeason, competitions: List[Competition], links: List[EventLink], status: Status) -> None:
        self.id = id
        self.uid = uid
        self.date = date
        self.name = name
        self.short_name = short_name
        self.season = season
        self.competitions = competitions
        self.links = links
        self.status = status

class EventsDate:
    date: str
    season_type: int

    def __init__(self, date: str, season_type: int) -> None:
        self.date = date
        self.season_type = season_type

class Logo:
    href: str
    width: int
    height: int
    alt: str
    rel: List[str]
    last_updated: str

    def __init__(self, href: str, width: int, height: int, alt: str, rel: List[str], last_updated: str) -> None:
        self.href = href
        self.width = width
        self.height = height
        self.alt = alt
        self.rel = rel
        self.last_updated = last_updated

class SeasonType:
    id: int
    type: int
    name: str
    abbreviation: str

    def __init__(self, id: int, type: int, name: str, abbreviation: str) -> None:
        self.id = id
        self.type = type
        self.name = name
        self.abbreviation = abbreviation

class LeagueSeason:
    year: int
    start_date: str
    end_date: str
    display_name: str
    type: SeasonType

    def __init__(self, year: int, start_date: str, end_date: str, display_name: str, type: SeasonType) -> None:
        self.year = year
        self.start_date = start_date
        self.end_date = end_date
        self.display_name = display_name
        self.type = type

class League:
    id: int
    uid: str
    name: str
    abbreviation: str
    midsize_name: str
    slug: str
    season: LeagueSeason
    logos: List[Logo]
    calendar_type: str
    calendar_is_whitelist: bool
    calendar_start_date: str
    calendar_end_date: str
    calendar: List[str]

    def __init__(self, id: int, uid: str, name: str, abbreviation: str, midsize_name: str, slug: str, season: LeagueSeason, logos: List[Logo], calendar_type: str, calendar_is_whitelist: bool, calendar_start_date: str, calendar_end_date: str, calendar: List[str]) -> None:
        self.id = id
        self.uid = uid
        self.name = name
        self.abbreviation = abbreviation
        self.midsize_name = midsize_name
        self.slug = slug
        self.season = season
        self.logos = logos
        self.calendar_type = calendar_type
        self.calendar_is_whitelist = calendar_is_whitelist
        self.calendar_start_date = calendar_start_date
        self.calendar_end_date = calendar_end_date
        self.calendar = calendar

class PurpleList:
    leagues: List[League]
    day: Day
    events: List[Event]
    events_date: EventsDate

    def __init__(self, leagues: List[League], day: Day, events: List[Event], events_date: EventsDate) -> None:
        self.leagues = leagues
        self.day = day
        self.events = events
        self.events_date = events_date
