# This is an automatically generated code sample.
# To make this code sample work in your Oracle Cloud tenancy,
# please replace the values for any parameters whose current values do not fit
# your use case (such as resource IDs, strings containing ‘EXAMPLE’ or ‘unique_id’, and
# boolean, number, and enum parameters with values not fitting your use case).


import oci

config = oci.config.from_file()
identity_client = oci.identity.IdentityClient(config)

tenancy_id = config["tenancy"]

# Get users from OCI
response = identity_client.list_users(compartment_id=tenancy_id)

# Print each user
for user in response.data:
    print(user)

# # Create a default config using DEFAULT profile in default location
# # Refer to
# # https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File
# # for more info
# config = oci.config.from_file()
#
#
# # Initialize service client with default config file
# identity_client = oci.identity.IdentityClient(config)
#
#
# # Send the request to service, some parameters are not required, see API
# # doc for more info
# list_users_response = identity_client.list_users(
#     compartment_id="ocid1.test.oc1..<unique_ID>EXAMPLE-compartmentId-Value",
#     page="EXAMPLE-page-Value",
#     limit=532,
#     identity_provider_id="ocid1.test.oc1..<unique_ID>EXAMPLE-identityProviderId-Value",
#     external_identifier="EXAMPLE-externalIdentifier-Value",
#     name="EXAMPLE-name-Value",
#     sort_by="NAME",
#     sort_order="ASC",
#     lifecycle_state="DELETED")
#
# # Get the data from response
# print(list_users_response.data)
