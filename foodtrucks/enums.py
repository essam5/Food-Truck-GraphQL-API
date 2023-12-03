from graphene import Enum

class StatusEnum(Enum):
    APPROVED = "APPROVED"
    REQUESTED = "REQUESTED"
    SUSPEND = "SUSPEND"
    EXPIRED = "EXPIRED"

class FacilityTypeEnum(Enum):
    PUSH_CART = "Push Cart"
    TRUCK = "Truck"