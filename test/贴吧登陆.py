import urllib.request

headers = {
    "Cookies":"BAIDUID=488CE0A294DA3184A556ECC4A0E228F3:FG=1; BIDUPSID=488CE0A294DA3184A556ECC4A0E228F3; PSINO=2; PSTM=1522214665; STOKEN=1ba8d3e1405c5fc5126f240d449bc6a05fafb606f4acb2841d5416f9341488c5; TIEBA_USERTYPE=35e5640d6ad0a98caa4e8c35; TIEBAUID=8609f3e2082b1b01cd1175b6; 638065370_FRSVideoUploadTip=1; bdshare_firstime=1523875616607; r_g=0; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; wise_device=0; H_PS_PSSID=26522_1465_26911_21108_22158; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1535425796,1535425801,1535426334,1535427387; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1535427479; BDUSS=Ut4N2hKdX5pZnd4a2RSZ29kd2hucVltR3dET1FMWEdiYmRGbX56MmoyUnZEMlZiQVFBQUFBJCQAAAAAAAAAAAEAAADaGggmZGF57MXQxAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAG-CPVtvgj1bY",
    "User-Agent ":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}
print(urllib.request.urlopen(urllib.request.Request(url="https://tieba.baidu.com/index.html",headers=headers)).read().decode())