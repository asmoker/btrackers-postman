# btrackers-postman

![](./logo.png)

BitTorrent Trackers Postman, fetch BitTorrent Trackers URL list from [ngosang/trackerslist](https://github.com/ngosang/trackerslist) and post to your aria2 server via jsonrpc.

## Usage
```bash
$ btp -h
usage: btp [-h] [-i index] [-p proxy] jsonrpc_url jsonrpc_token

positional arguments:
  jsonrpc_url           Target aria2 server jsonrpc url
  jsonrpc_token         Target aria2 server jsonrpc token

optional arguments:
  -h, --help            show this help message and exit
  -i index, --index index
                        0 - trackers_best (DEFAULT)
                        1 - trackers_all
                        2 - trackers_all_udp
                        3 - trackers_all_http
                        4 - trackers_all_https
                        5 - trackers_best_ip
                        6 - trackers_all_ip
                        More detail: https://github.com/ngosang/trackerslist
  -p proxy, --proxy proxy
                        Request proxy, http proxy or socks proxy likes:
                        http://user:password@10.1.1.6:8080 or socks5://127.0.0.1:1086
```

## License

The library is available as open source under the terms of the [Apache-2.0](https://opensource.org/licenses/Apache-2.0).