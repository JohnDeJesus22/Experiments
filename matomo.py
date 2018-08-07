import json
from piwikapi.analytics import PiwikAnalytics

# get live data
pa = PiwikAnalytics()
pa.set_api_url('https://audiobook.innocraft.cloud/index.php')
pa.set_id_site(1) # 1 is the side ID you want to log to
pa.set_format('json')
pa.set_period('day')
pa.set_date('today')
pa.set_method('Live.getLastVisitsDetails')
pa.set_parameter('lastMinutes', 5)
visits = json.loads(pa.send_request())
#generates error in the variable explorer
# "You can't access this resource as it requires 'view' access for the website id = 1."

# attempt for getting image graph. Runs but does not return image.
from piwikapi.analytics import PiwikAnalytics

pa = PiwikAnalytics()
pa.set_api_url('https://audiobook.innocraft.cloud/index.php')
pa.set_id_site(1) # 1 is the side ID you want to log to
pa.set_method('ImageGraph.get')
pa.set_parameter('apiModule', 'UserCountry')
pa.set_parameter('apiAction', 'getCountry')
image = pa.send_request()