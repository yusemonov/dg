import CloudFlare


def main():
    cf = CloudFlare.CloudFlare(
        email='whitetech.lp@gmail.com', token='ff029fbbc9b791bac44bba34f88b3738bea3f')
    zones = cf.zones.get()
    for zone in zones:
        print(zone.keys())
    # for zone in zones:
    #     zone_id = zone['id']
    #     zone_name = zone['name']

    #     settings_ssl = cf.zones.settings.ssl.get(zone_id)
    #     ssl_status = settings_ssl['value']

    #     settings_ipv6 = cf.zones.settings.ipv6.get(zone_id)
    #     ipv6_status = settings_ipv6['value']

    #     # print(zone_id, zone_name, ssl_status, ipv6_status)
    #     print(zone_id)


if __name__ == '__main__':
    main()
