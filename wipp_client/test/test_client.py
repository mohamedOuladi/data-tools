# Test script
# Demonstrates examples of client use
# Requires python-keycloak to be installed (`pip install python-keycloak`)
# Please fill in the relevant `keycloak_server_url`, `username`, `password`

from keycloak import KeycloakOpenID
from wipp_client import (
    Wipp,
    WippImageCollection,
    WippCsvCollection,
    WippGenericDataCollection,
    WippPlugin,
    WippStitchingVector,
    WippPyramidAnnotation
)


# Configure Keycloak client
keycloak_openid = KeycloakOpenID(
    server_url="http://localhost:8081/auth/",
    client_id="wipp-public-client",
    realm_name="WIPP",
)

# Get Token
token = keycloak_openid.token("simo-admin", "123")

# Test that token is valid in Keycloak by getting some information about the user
userinfo = keycloak_openid.userinfo(token["access_token"])
print(f"Keycloak user: {userinfo['preferred_username']}")


# Create WIPP client
w = Wipp()

# Configure Keycloak token in the client
# w.auth_headers = token["access_token"]

### Test client functionality ###

# Create Image Collection
ic = WippImageCollection(name="Test Image collection")
# nic = w.create_image_collection(ic)
# print(f"Created Image Collection: {nic.id}")

# for c in w.get_image_collections():
#     print(c)

# print(f"Deleted Image Collection: {nic.id}")
# w.delete_image_collection(nic.id)

# for c in w.get_image_collections():
#     print(c)

# Create Stitching Vector
print("Testing..!")
# stitching_vector = WippStitchingVector(name = "Test-stitching-vector")
# created_stitching_vector = w.create_stitching_vector(stitching_vector)

# print(f"Created Stitching Vector: {created_stitching_vector.id}")


# for c in w.get_image_collections_images('60a3056bbbdc874aefc8e22e'):
#     print(c)

# print(w.get_image_collections_images('61dc658f9f68996e2427cdcb'))
# print(w.get_stitching_vector_time_slices('6112cecd0947a13ef42523ee'))
# w.delete_stitching_vector('6112cee80947a13ef42523ef')

print(w.get_image_collections_images('61ccbb546fa1f65bf8cd0f11'))
print(w.get_pyramid_annotation_time_slices('5f4e9ef798cee418b81f19c0'))


# for c in w.get_stitching_vector_time_slices("6112bc560947a13ef42523e9"):
#     print(c)

# print(f"Deleted Generic Data: {created_generic_data_collection.id}")
# w.delete_generic_data_collection(created_generic_data_collection.id)

# for c in w.get_generic_data_collections():
#     print(c)

# Create CSV collection
# csv_collection = WippCsvCollection(name="Test CSV collection")
# created_csv_collection = w.create_csv_collection(csv_collection)

# print(f"Created CSV Collection: {created_csv_collection.id}")

# for c in w.get_csv_collections():
#     print(c)

# print(f"Deleted CSV Collection: {created_csv_collection.id}")
# w.delete_csv_collection(created_csv_collection.id)

# for c in w.get_csv_collections():
#     print(c)

# Create Generic Data Collection (does not work in API yet)
# generic_data_collection = WippGenericDataCollection(name = "Test Generic Data Collection")
# created_generic_data_collection = w.create_generic_data_collection(generic_data_collection)

# print(f"Created Generic Data Collection: {created_generic_data_collection.id}")

# for c in w.get_generic_data_collections():
#     print(c)

# print(f"Deleted Generic Data: {created_generic_data_collection.id}")
# w.delete_generic_data_collection(created_generic_data_collection.id)

# for c in w.get_generic_data_collections():
#     print(c)

# Crerate plugin object
plugin = {
    "name": "WIPP API Test",
    "version": "0.0.5",
    "containerId": "ktaletsk/noop",
    "title": "Test Plugin Created by Python WIPP API client 0.0.5",
    "description": "This plugin does nothing",
    "author": "Konstantin Taletskiy (konstantin.taletskiy@labshare.org)",
    "institution": "National Center for Advancing Translational Sciences, National Institutes of Health",
    "repository": "https://github.com/labshare/polus-plugins",
    "website": "",
    "citation": "",
    "inputs": [
        {
            "name": "inpImageDir",
            "description": "Input Image collection to make predictions on",
            "type": "collection",
            "required": True,
        },
        {
            "name": "inpBaseDir",
            "description": "Input SplineDist Model that contains weights",
            "type": "genericData",
            "required": True,
        },
        {
            "name": "imagePattern",
            "description": "Pattern of the images in Input",
            "type": "string",
            "required": False,
        },
    ],
    "outputs": [
        {
            "name": "outDir",
            "description": "Output Directory for Predicted Images",
            "type": "genericData",
            "required": True,
        }
    ],
    "ui": [
        {
            "key": "inputs.inpImageDir",
            "title": "Input Image Directory: ",
            "description": "Collection name that contains intensity based images",
        },
        {
            "key": "inputs.inpBaseDir",
            "title": "Model Directory: ",
            "description": "Directory containing the model weights and config file",
        },
        {
            "key": "inputs.imagePattern",
            "title": "Image Pattern: ",
            "description": "Pattern of images in input collection (image_r{rrr}_c{ccc}_z{zzz}.ome.tif). ",
        },
    ],
}

# wp = WippPlugin(**plugin)

# # Register plugin
# np = w.create_plugin(wp)
# print(np)
# print(f"Registered plugin: {np.id}")

# for p in w.get_plugins():
#     print(p)

# # Delete plugin
# w.delete_plugin(np.id)
# print(f"Deleted plugin: {np.id}")
