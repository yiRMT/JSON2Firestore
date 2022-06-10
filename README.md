# JSON2Firestore
## Requirements
### Python Modules
* Python <= 3.9 (**don't work with 3.10 or later!!!**)
* firebase_admin

### Firebase
Download `ServiceAccountKey.json` from Firebase console and place it in the root directory.

## How to use
* Place JSON files in `/json` directory.
* `parse_json_files(filename)` is a function which converts a JSON file to a dictionary type. You don't need to edit this function unless you need to customize data in advance.
* `upload_to_firestore()` is a function which uploads a dictionary (which is a map type in Firestore) to Firestore. `parse_json_files(filename)` is called inside this function. **You need to edit Firestore directory path.**

## License
This repository is available under the MIT license.