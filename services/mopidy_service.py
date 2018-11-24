# import json
# import urllib.parse
# from services.parent_service import ParentService
# import requests
# import time
# from mopidy_json_client import MopidyClient
#
# class MopidyService(ParentService):
#
#     def __init__(self, ip=None, username=None, password=None):
#         self.ip = ip
#         self.username = username
#         self.password = password
#         self.mopidy_url = " http://192.168.0.14:6680/mopidy/rpc"
#
#
#     def get_info(self):
#         data = {
#                   "method": "core.get_uri_schemes",
#                   "jsonrpc": "2.0",
#                   "params": {},
#                   "id": 1
#                 }
#         url = "http://192.168.0.14:6680/mopidy/rpc"
#         response = self.send_http(url, data)
#         string = response.json()
#
#     def clear_tracklist(self):
#         url = " http://192.168.0.14:6680/mopidy/rpc"
#         data = {
#                   "method": "core.tracklist.clear",
#                   "jsonrpc": "2.0",
#                   "params": {},
#                   "id": 1
#                 }
#         self.send_http(url=url, data=data)
#
#     def add_playlist_tracklist(self, playlist_name=None):
#         playlist_uri = ""
#         data = {
#               "method": "core.playlists.as_list",
#               "jsonrpc": "2.0",
#               "params": {},
#               "id": 1
#             }
#         track_response = self.send_http(data=data)
#         if(track_response.status_code== 200):
#             playlist_tracks = track_response.json()
#             for playlist in playlist_tracks['result']:
#                 if playlist['name'].lower() == playlist_name.lower():
#                     playlist_uri = playlist['uri']
#
#         track_uri = []
#
#         data =  {
#                     "method": "core.playlists.get_items",
#                     "jsonrpc": "2.0",
#                     "params": {
#                         "uri": playlist_uri
#                     },
#                     "id": 1
#                   }
#
#         dummy_track = {}
#         alltrack_response = self.send_http(data=data)
#         playlist_tracks =  playlist_tracks = alltrack_response.json()
#         for track in playlist_tracks['result']:
#             track_uri.append(track['uri'])
#             dummy_track = track
#         url = urllib.parse.unquote(dummy_track['uri']).decode('utf8')
#
#         {
#             "method": "core.tracklist.add",
#             "jsonrpc": "2.0",
#             "params": {
#                  "uris":dummy_track
#             },
#             "id": 1
#         }
#
#         add_track_list_response = self.send_http(data=data)
#
#         print("dum,m,y")
#
#
#     def test(self):
#
#         self.mopidy = MopidyClient(
#             ws_url='ws://localhost:6680/mopidy/ws',
#             error_handler=None,
#             connection_handler=None,
#             autoconnect=False,
#             retry_max=10,
#             retry_secs=10
#         )
#
#         self.mopidy.connect()
#         args = ""
#         self.mopidy.tracklist.add(uris=self.gen_uris(args))
#
#     def on_connection(self, conn_state):
#         if conn_state:
#             # Initialize mopidy track and state
#             self.state = self.mopidy.playback.get_state(timeout=5)
#             tl_track = self.mopidy.playback.get_current_tl_track(timeout=15)
#             self.track_playback_started(tl_track)
#         else:
#             self.state = 'stopped'
#             self.uri = None
#
#
#
#     def send_http(self, url=None, data=None):
#         if(not url):
#             url = self.mopidy_url
#
#         r = requests.post(url, auth=('username', 'password'), verify=False, json=data,
#                           headers={"content-type": "application/json"})
#         time.sleep(1)
#         return r
#
