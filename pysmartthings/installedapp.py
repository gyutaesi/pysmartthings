"""Define the installedapp module."""

from enum import Enum
from typing import Sequence

from .api import API
from .entity import Entity


class InstalledAppType(Enum):
    """Define the type of installed app."""

    UNKNOWN = "UNKNOWN"
    LAMBDA_SMART_APP = 'LAMBDA_SMART_APP'
    WEBHOOK_SMART_APP = 'WEBHOOK_SMART_APP'
    BEHAVIOR = 'BEHAVIOR'


class InstalledAppStatus(Enum):
    """Define the installed app status."""

    UNKNOWN = "UNKNOWN"
    PENDING = "PENDING"
    AUTHORIZED = "AUTHORIZED"
    REVOKED = "REVOKED"
    DISABLED = "DISABLED"


class InstalledApp:
    """Define the InstalledApp class."""

    _installed_app_id: str
    _installed_app_type: InstalledAppType
    _installed_app_status: InstalledAppStatus
    _display_name: str
    _app_id: str
    _reference_id: str
    _location_id: str
    _createdDate: str
    _lastUpdatedDate: str
    _classifications: Sequence[str]

    def __init__(self):
        """Create a new instance of the InstalledApp class."""
        self._installed_app_id = None
        self._installed_app_type = InstalledAppType.UNKNOWN
        self._installed_app_status = InstalledAppStatus.UNKNOWN
        self._display_name = None
        self._app_id = None
        self._reference_id = None
        self._location_id = None
        self._created_date = None
        self._last_updated_date = None
        self._classifications = []

    def apply_data(self, data: dict):
        """Apply the data structure to the properties."""
        self._installed_app_id = data['installedAppId']
        self._installed_app_type = InstalledAppType(data['installedAppType'])
        self._installed_app_status = \
            InstalledAppStatus(data['installedAppStatus'])
        self._display_name = data['displayName']
        self._app_id = data['appId']
        self._reference_id = data['referenceId']
        self._location_id = data['locationId']
        self._created_date = data['createdDate']
        self._last_updated_date = data['lastUpdatedDate']
        self._classifications = data['classifications']

    @property
    def installed_app_id(self) -> str:
        """Get the ID of the installed app."""
        return self._installed_app_id

    @property
    def installed_app_type(self) -> InstalledAppType:
        """Get the type of installed app."""
        return self._installed_app_type

    @property
    def installed_app_status(self) -> InstalledAppStatus:
        """Get the current state of an install."""
        return self._installed_app_status

    @property
    def display_name(self) -> str:
        """Get the user defined name for the installed app."""
        return self._display_name

    @property
    def app_id(self) -> str:
        """Get the ID of the app."""
        return self._app_id

    @property
    def reference_id(self) -> str:
        """Get a reference to an upstream system."""
        return self._reference_id

    @property
    def location_id(self) -> str:
        """Get the ID of the location to which the installed app."""
        return self._location_id

    @property
    def created_date(self) -> str:
        """Get the date the installed app was created."""
        return self._created_date

    @property
    def last_updated_date(self) -> str:
        """Get the date the installed app was updated."""
        return self._last_updated_date

    @property
    def classifications(self) -> Sequence[str]:
        """Get the collection of classifications."""
        return self._classifications


class InstalledAppEntity(Entity, InstalledApp):
    """Define the InstalledAppEntity class."""

    def __init__(self, api: API, data=None, installed_app_id=None):
        """Create a new instance of the InstalledAppEntity class."""
        Entity.__init__(self, api)
        InstalledApp.__init__(self)
        if data:
            self.apply_data(data)
        if installed_app_id:
            self._installed_app_id = installed_app_id

    def refresh(self):
        """Refresh the installedapp information using the API."""
        data = self._api.get_installedapp(self._installed_app_id)
        self.apply_data(data)

    def save(self):
        """Save the changes made to the app."""
        raise NotImplementedError