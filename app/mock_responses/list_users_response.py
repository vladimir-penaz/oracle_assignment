import datetime
import oci.identity.models

list_users = [
    oci.identity.models.User(
        id="ocid1.user.oc1..aaaaaaaaxyz",
        name="johndoe",
        time_created=datetime.datetime(2023, 11, 1, 12, 34, 56),
        compartment_id="ocid1.tenancy.oc1..example",
        email="peny753@seznam.cz",
        lifecycle_state="ACTIVE",
        description="John Doe",
        inactive_status=None,
        freeform_tags={},
        defined_tags={}
    ),
    oci.identity.models.User(
        id="ocid1.user.oc1..ccccccghijkl",
        name="alicew",
        time_created=datetime.datetime(2022, 11, 3, 9, 45, 30),
        compartment_id="ocid1.tenancy.oc1..tenant456",
        email="peny753@seznam.cz",
        lifecycle_state="ACTIVE",
        description="Alice Williams",
        inactive_status=None,
        freeform_tags={},
        defined_tags={}
    ),
    oci.identity.models.User(
        id="ocid1.user.oc1..eeeeeeuvwxyz",
        name="sarahj",
        time_created=datetime.datetime(2020, 12, 5, 12, 10, 5),
        compartment_id="ocid1.tenancy.oc1..tenant999",
        email="peny753@seznam.cz",
        lifecycle_state="ACTIVE",
        description="Sarah Johnson",
        inactive_status=None,
        freeform_tags={},
        defined_tags={}
    ),
    oci.identity.models.User(
        id="ocid1.user.oc1..ddddddmnopqr",
        name="bobm",
        time_created=datetime.datetime(2021, 7, 21, 16, 20, 15),
        compartment_id="ocid1.tenancy.oc1..tenant789",
        email="peny753@seznam.cz",
        lifecycle_state="ACTIVE",
        description="Bob Miller",
        inactive_status=None,
        freeform_tags={},
        defined_tags={}
    )
]
