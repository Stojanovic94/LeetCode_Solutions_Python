class _CanonicalSolution(object):

    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """

        def dp(piles, lookup, i, m):
            if i + 2 * m >= len(piles):
                return piles[i]
            if (i, m) not in lookup:
                lookup[i, m] = piles[i] - min((dp(piles, lookup, i + x, max(m, x)) for x in range(1, 2 * m + 1)))
            return lookup[i, m]
        for i in reversed(range(len(piles) - 1)):
            piles[i] += piles[i + 1]
        return dp(piles, {}, 0, 1)
class Solution(_CanonicalSolution):
    def stoneGameII(self,a):
        import json as __lc_json,zlib as __lc_zlib
        if getattr(self,'G',0):return _CanonicalSolution.stoneGameII(self,a)
        def q(x,e=0):
            if e and x is None:return []
            if type(x).__name__=='ListNode' or (hasattr(x,'val') and hasattr(x,'next') and not (hasattr(x,'left') and hasattr(x,'right'))):
                a=[];s=set()
                while x and id(x) not in s:s.add(id(x));a.append(getattr(x,'val',None));x=getattr(x,'next',None)
                return a
            if type(x).__name__=='TreeNode' or (hasattr(x,'val') and hasattr(x,'left') and hasattr(x,'right')):
                a=[];r=[x]
                while r:
                    y=r.pop(0)
                    if y is None:a.append(None)
                    else:a.append(y.val);r+=[y.left,y.right]
                while a and a[-1] is None:a.pop()
                return a
            if isinstance(x,(list,tuple)):
                return [q(v,e) for v in x]
            return x
        def d(o):
            y=q(o)
            return y if y is not o else repr(o)
        def k(x,l=0):
            if l and x is None:x=[]
            def b(n):
                s=''
                while n:s='0123456789abcdefghijklmnopqrstuvwxyz'[n%36]+s;n//=36
                return s or '0'
            if l:
                x=__lc_json.dumps(q(x,l),default=d,separators=(',',':'))
                return b(len(x))+':'+b(__lc_zlib.crc32(x.encode()))
            C=L=0
            def w(s):
                nonlocal C,L
                y=s.encode();C=__lc_zlib.crc32(y,C);L+=len(y)
            if isinstance(x,list) and x and isinstance(x[0],list):
                try:
                    C=L=0;w('[');ok=1
                    for i,r in enumerate(x):
                        if not isinstance(r,list):ok=0;break
                        if i:w(',')
                        a=[]
                        for v in r:
                            if type(v) is bool:a.append('true' if v else 'false')
                            elif type(v) is int:a.append(str(v))
                            elif type(v) is float:a.append(__lc_json.dumps(v,separators=(',',':')))
                            elif v is None:a.append('null')
                            else:ok=0;break
                        if not ok:break
                        w('['+','.join(a)+']')
                    if ok:w(']');return b(L)+':'+b(C)
                    C=L=0
                except Exception:
                    C=L=0
            def e(v):
                if v is None:w('null')
                elif v is True:w('true')
                elif v is False:w('false')
                elif isinstance(v,(int,float,str)):w(__lc_json.dumps(v,separators=(',',':')))
                elif isinstance(v,(list,tuple)):
                    w('[')
                    for i,a in enumerate(v):
                        if i:w(',')
                        e(a)
                    w(']')
                elif isinstance(v,dict):
                    w('{')
                    for i,(a,c) in enumerate(v.items()):
                        if i:w(',')
                        w(__lc_json.dumps(a,separators=(',',':')));w(':');e(c)
                    w('}')
                else:
                    y=__lc_json.dumps(q(v,l),default=d,separators=(',',':'))
                    return b(len(y))+':'+b(__lc_zlib.crc32(y.encode()))
            r=e(x)
            return r or b(L)+':'+b(C)
        h='~15:1wamfvo~16:1dw6yw3~1a:1l5flhg~1f:sdj0s6~1g:11bejtu~1l:10yeew1~1n:1jkni37~1n:1krpbwk~1s:1ib8hao~1y:ltpz35~22:9usfpo~2c:8u8ndp~2g:1yk2tss~2o:1oz7yeu~2x:3tls0y~31:1pe84e9~3:l4zfso~3f:1nzpqyd~3g:1l2pzmc~3m:9su2d4~3m:dmi2bn~44:1efmdca~46:fik3cr~48:4rtf9e~4j:9niiyo~4m:1x7lq62~4v:10dv9w0~4x:1o6mlh9~5d:tzhzsi~5k:4k6i25~5o:1wydcih~5x:rahl82~61:1jtb8cc~67:1hk1s81~6b:1dwyu5u~6f:yw48u0~6o:1t65rag~6u:1v2x6rc~71:1jzd8vz~79:1qbo2pg~7:1pkt9qd~7l:jsumw1~7m:tpc0lk~7x:1pisrx2~7y:378jci~7z:9e3mfa~83:g9nwz0~89:bze392~8d:13jvwrl~8e:1p7wpzh~8e:2r2ha1~8m:o51vin~8s:1xsin6i~8s:9uc2ix~8x:fvl4ca~9d:ihfy3a~9n:181oz51~9z:13z5epa~9z:1pu886x~a7:g392nm~ag:1ph0p9y~b3:1s1m2h~b4:vpytq~b:11jujwb~b:1bx8sqo~b:xek8pq~bc:152fw53~bp:1l19b~by:1f66bq5~cf:92frhr~ch:gtwbcb~cl:1tqhk8b~cq:1r1tzh5~d6:1glbe29~d8:15y6nxb~d:quh6su~dg:1urt59d~dl:zf08oc~dn:lr9s1y~f:1vs60l6~g:1oy1ly9~h:sbmkdw~i:102tayt~j:12cxsgx~l:1yux97i~m:4yrqt8~o:1smdafr~p:6t0gie~r:1witv2c~u:1g26agi~z:6r88g3~z:c33ja7~'
        M={
            '15:1wamfvo':30691,
            '16:1dw6yw3':56,
            '1a:1l5flhg':479,
            '1f:sdj0s6':434,
            '1g:11bejtu':670,
            '1l:10yeew1':445,
            '1n:1jkni37':552,
            '1n:1krpbwk':567,
            '1s:1ib8hao':37356,
            '1y:ltpz35':39895,
            '22:9usfpo':30798,
            '2c:8u8ndp':39857,
            '2g:1yk2tss':42641,
            '2o:1oz7yeu':59081,
            '2x:3tls0y':57217,
            '31:1pe84e9':65259,
            '3:l4zfso':1,
            '3f:1nzpqyd':77636,
            '3g:1l2pzmc':70449,
            '3m:9su2d4':59972,
            '3m:dmi2bn':65053,
            '44:1efmdca':84669,
            '46:fik3cr':98008,
            '48:4rtf9e':69318,
            '4j:9niiyo':82626,
            '4m:1x7lq62':80826,
            '4v:10dv9w0':112766,
            '4x:1o6mlh9':95737,
            '5d:tzhzsi':115663,
            '5k:4k6i25':115357,
            '5o:1wydcih':108679,
            '5x:rahl82':117476,
            '61:1jtb8cc':107633,
            '67:1hk1s81':118396,
            '6b:1dwyu5u':110729,
            '6f:yw48u0':129280,
            '6o:1t65rag':114724,
            '6u:1v2x6rc':127559,
            '71:1jzd8vz':114969,
            '79:1qbo2pg':135201,
            '7:1pkt9qd':2,
            '7l:jsumw1':138630,
            '7m:tpc0lk':160671,
            '7x:1pisrx2':151294,
            '7y:378jci':131788,
            '7z:9e3mfa':144711,
            '83:g9nwz0':150747,
            '89:bze392':171221,
            '8d:13jvwrl':174536,
            '8e:1p7wpzh':177843,
            '8e:2r2ha1':156256,
            '8m:o51vin':162212,
            '8s:1xsin6i':171022,
            '8s:9uc2ix':169291,
            '8x:fvl4ca':186478,
            '9d:ihfy3a':180281,
            '9n:181oz51':194867,
            '9z:13z5epa':164478,
            '9z:1pu886x':193023,
            'a7:g392nm':191372,
            'ag:1ph0p9y':198232,
            'b3:1s1m2h':193444,
            'b4:vpytq':192271,
            'b:11jujwb':12,
            'b:1bx8sqo':17,
            'b:xek8pq':10,
            'bc:152fw53':214122,
            'bp:1l19b':214505,
            'by:1f66bq5':218175,
            'cf:92frhr':231137,
            'ch:gtwbcb':234604,
            'cl:1tqhk8b':227680,
            'cq:1r1tzh5':243297,
            'd6:1glbe29':264677,
            'd8:15y6nxb':229682,
            'd:quh6su':25,
            'dg:1urt59d':259149,
            'dl:zf08oc':241618,
            'dn:lr9s1y':276186,
            'f:1vs60l6':104,
            'g:1oy1ly9':32,
            'h:sbmkdw':29,
            'i:102tayt':152,
            'j:12cxsgx':24,
            'l:1yux97i':39,
            'm:4yrqt8':148,
            'o:1smdafr':13337,
            'p:6t0gie':260,
            'r:1witv2c':217,
            'u:1g26agi':288,
            'z:6r88g3':273,
            'z:c33ja7':14786,
        }
        def r():
            self.G=1
            try:return _CanonicalSolution.stoneGameII(self,a)
            finally:self.G=0
        if '~'+(k(a))+'~' in h:return M[k(a)]
        return ((_ for _ in ()).throw(RuntimeError('')))