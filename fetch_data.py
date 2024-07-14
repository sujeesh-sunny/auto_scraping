import requests
import json
from datetime import datetime

HEADERS = {
    'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
    'Cookie':  "ajs_anonymous_id=33183b74-475b-4f1f-937a-d4c903166054; AMCVS_68B620B35350F1650A490D45%40AdobeOrg=1; _pin_unauth=dWlkPU9UaGhNVGswTWpFdFpHWmpPUzAwWVdOa0xUZ3dZMkl0TW1FeVpqTTFaVGM0TXpBMg; wfm.tracking.sessionStart=1707115142229; sa-user-id=s%253A0-e09a6035-dbb5-5e72-6b55-d4a3d3151d09.WK86YvxnZaUk2O8ll%252FOSaJxdVCJWK6v2%252FMo%252B86BXRTo; sa-user-id-v2=s%253A4JpgNdu1XnJrVdSj0xUdCTEvxIg.OsMBR8tfqvcRCZQZMgco%252BASkDbGnoOEQX8tIn%252BvQjqk; sa-user-id-v3=s%253AAQAKIPKv96fHV4WdcPyxHZU-JjNyp1oVxB6O7vrm6gYp1lxTEAEYAyDVvLmsBjABOgROQQ4MQgT5oNN3.azv4yw2dCUXGVQGQrSFzNh%252FOh7lIuF0%252BBt1j5UyoYMw; __stripe_mid=df9962f1-2f54-4604-bc12-c105a3e092882ff550; wfm.tracking.s10=1; ajs_anonymous_id=33183b74-475b-4f1f-937a-d4c903166054; wfm.tracking.x2p=1; at_check=true; _pin_unauth=dWlkPU9UaGhNVGswTWpFdFpHWmpPUzAwWVdOa0xUZ3dZMkl0TW1FeVpqTTFaVGM0TXpBMg; at_check=true; __cf_bm=BThBRatRdpDsCOSXxWhX0gT9lmC_JxZPxTkG1vOfHVI-1720934009-1.0.1.1-I972SANIhhm29X1lhWqogIPKuhIUcj4sztBG9RYRoE5rjSTOonfiYqUeIU0SXVKJwLGYxwc03CpUWwMwx_ZFxQ; kndctr_68B620B35350F1650A490D45_AdobeOrg_identity=CiY0NjQ5NTU5MTIxODI0NjUwMDk1MTk2MzEyMDc4MDcyNzI4MDU3MVIRCIC697_XMRgBKgRJTkQxMAPwAci6t_2KMg==; kndctr_68B620B35350F1650A490D45_AdobeOrg_cluster=ind1; AMCV_68B620B35350F1650A490D45%40AdobeOrg=179643557%7CMCIDTS%7C19919%7CMCMID%7C46495591218246500951963120780727280571%7CMCAAMLH-1721539125%7C12%7CMCAAMB-1721539125%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1720941525s%7CNONE%7CMCSYNCSOP%7C411-19926%7CvVersion%7C5.5.0%7CMCCIDH%7C0; _fbp=fb.1.1720934326127.104198625507211616; _gcl_au=1.1.1710969402.1720934327; wfmStoreId=16; inRedirectTestAudience=1; inChampagneRedirectAudience=1; inRedirectGoldPanAudience=1; inRedirectGlutenFreeAudience=1; inRedirectVitaminsAudience=1; lux_uid=172093438750018449; __stripe_sid=c024fc5e-9b25-44e0-a8e0-f6396df5e5e4426690; _derived_epik=dj0yJnU9WGF0RGlsZ0Jac2tmU0NheUFzUmRXN0I0dXZoZkczVzUmbj1waFJ0RHUwS3UxRU5QV05SZUxvaVFnJm09MSZ0PUFBQUFBR2FUWUxnJnJtPTEmcnQ9QUFBQUFHYVRZTGcmc3A9Mg; dotcomSearchId=dd71d805-789a-417f-b4c0-079a27cb0aef; s_gpv=Search%20Results:%20apple%20|%20Wegmans; _uetsid=8bef37d041a011ef9e4197ee113cbb6a; _uetvid=3f99e440c3f111eebd48914dcddadd20; _derived_epik=dj0yJnU9MUhNaHdGbXhXeHBCSEp0RDduREFwUUNhMGZhejcyQmYmbj1Zdm00X00yeWNqRmZHb3ZvYzY4eVl3Jm09MSZ0PUFBQUFBR2FUWVNRJnJtPTEmcnQ9QUFBQUFHYVRZU1Emc3A9Mg; session-prd-weg=.eJwdjstygjAAAP8lZ-vw0LZwFXUSSSgOGOXCIIQSApEhYBs6_fdmetjLXnZ_QF6PTDXAr4tOsRXIBzb2hWRyAv40zsYophR_yHx6CCaBD5hGzf1Y8ogjmC7QJhx5ayPt0rlow1I63fPeeUO2g6-wxVaWlDprUR8m6UKCciJH1N-0tSEOEmFSiYxi-0Zji7RIkB1UUF6W7IrqgsY8auMtXtIlCuAX0V_8Rs9TQbf_ravTCdgOc0W_VbgzU703M2o_qyvmkTzriqYK9l1TmQ9sHnAgTB9r4lrrIczPpZd9SHHiddDE7nOftCesLIJ6ZuvLYd-1BxVl6OUTrMCs2JjzCvgbz92674719vsHtRhqtA.GXTypA.pVyZDqI4m8-51PRsgD5WXJ7qlXc; _dd_s=rum=0&expire=1720935592500; mbox=session#26d636fe866f4747a3f5aee22690fd56#1720936553|PC#26d636fe866f4747a3f5aee22690fd56.41_0#1784179410"
}

def fetch_data():
    url = "https://shop.wegmans.com/api/v2/store_products?fulfillment_type=instore&ads_enabled=true&ads_pagination_improvements=true&limit=60&offset=0&page=1&prophetScorer=frecency&sort=rank&allow_autocorrect=true&search_is_autocomplete=false&search_provider=ic&search_term=apple&secondary_results=true&unified_search_shadow_test_enabled=false"

    response = requests.get(url, headers=HEADERS)
    data = response.json()

    print("Response keys:", data.keys())

    if response.status_code == 401:
        print("Unauthorized access. Please check your API key or cookie settings.")
        return

    filename = f"data_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"
    with open(filename, 'w') as file:
        json.dump(data, file)

    process_data(filename)


def process_data(filename):
    import process_data
    process_data.process_and_store_data(filename)

if __name__ == "__main__":
    fetch_data()
