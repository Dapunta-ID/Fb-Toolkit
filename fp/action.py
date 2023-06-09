from fp.modul import *

def wait():
    times = 45
    while True:
        if times < 10:
            print(f'{u} --> {p}Tunggu{m} 0{times}', end='\r')
        else:
            print(f'{u} --> {p}Tunggu{m} {times}', end='\r')
        times -=1
        time.sleep(1)
        if times == 0:break
        
#1

def massAFR():
    print(f'\n{p} Mass Confirm Friend Request is{h} Running!!!')
    print(o +' ----------------------------------------')
    num = 1
    __cookies = {'cookie':open('user/.cookies', 'r').read()}
    link = ['https://mbasic.facebook.com/friends/center/requests/#friends_center_main']
    with r.Session() as ses:
        for url in link:
            page = bs(ses.get(url, cookies=__cookies).text, 'html.parser')
            for tbody in page.find_all('tbody'):
                if 'Konfirmasi' in str(tbody):
                    data = {}
                    for user in tbody.find_all('a'):
                        if '/friends/hovercard/mbasic/?' in str(user):
                            data.update({'name':user.text, 'id':user['href'].split('=')[1].split('&')[0]})
                        elif '/a/notifications.php?confirm' in str(user):
                            data.update({'url':'https://mbasic.facebook.com/'+ user['href']})
                    lanjut = page.find('a', string='Lihat selengkapnya')
                    if lanjut is None:pass
                    else:
                        link.append('https://mbasic.facebook.com/'+ lanjut['href'])
                    post = ses.get(data['url'], cookies=__cookies).text
                    if 'Permintaan diterima' in str(post):
                        print(f' {u}[ {p}{data["name"]}|{data["id"]}{u} ] {h}Berhasil Dikonfirmasi {m}{num}')
                        num +=1
                    else:
                        print(f' {u}[ {p}{data["name"]}|{data["id"]}{u} ] {m}Gagal Dikonfirmasi')
                    wait()
            lanjut = page.find('a', string='Lihat selengkapnya')
            if lanjut is None:pass
            else:
                link.append('https://mbasic.facebook.com/'+ lanjut['href'])

def massDFR():
    print(f'\n{p} Mass Delete Friend Request is{h} Running!!!')
    print(o +' ----------------------------------------')
    num = 1
    __cookies = {'cookie':open('user/.cookies', 'r').read()}
    link = ['https://mbasic.facebook.com/friends/center/requests/#friends_center_main']
    with r.Session() as ses:
        for url in link:
            page = bs(ses.get(url, cookies=__cookies).text, 'html.parser')
            for tbody in page.find_all('tbody'):
                if 'Konfirmasi' in str(tbody):
                    data = {}
                    for user in tbody.find_all('a'):
                        if '/friends/hovercard/mbasic/?' in str(user):
                            data.update({'name':user.text, 'id':user['href'].split('=')[1].split('&')[0]})
                        elif '/a/notifications.php?delete' in str(user):
                            data.update({'url':'https://mbasic.facebook.com/'+ user['href']})
                    lanjut = page.find('a', string='Lihat selengkapnya')
                    if lanjut is None:pass
                    else:
                        link.append('https://mbasic.facebook.com/'+ lanjut['href'])
                    post = ses.get(data['url'], cookies=__cookies).text
                    if 'Permintaan diterima' in str(post):
                        print(f' {u}[ {p}{data["name"]}|{data["id"]}{u} ] {h}Berhasil Dihapus {m}{num}')
                        num +=1
                    else:
                        print(f' {u}[ {p}{data["name"]}|{data["id"]}{u} ] {m}Gagal Dihapus')
                    wait()
            lanjut = page.find('a', string='Lihat selengkapnya')
            if lanjut is None:pass
            else:
                link.append('https://mbasic.facebook.com/'+ lanjut['href'])

def massAFFS():
    print(f'\n{p} Mass Auto Add From Suggestion is{h} Running!!!')
    print(o +' ----------------------------------------')
    num = 1
    __cookies = {'cookie':open('user/.cookies', 'r').read()}
    nex = ['https://mbasic.facebook.com/friends/center/mbasic']
    with r.Session() as ses:
        for url in nex:
            page = bs(ses.get(url, cookies=__cookies).text, 'html.parser')
            for tbody in page.find_all('tbody'):
                if '/friends/hovercard/mbasic/' in str(tbody):
                    if 'Tambah Teman' in str(tbody):
                        target = {}
                        for nm in tbody.find_all('a'):
                            if '/friends/hovercard/mbasic/' in str(nm):
                                target.update({'name':nm.text, 'uid':nm['href'].split('=')[1].split('&')[0]})
                        for nmx in tbody.find('tbody').find_all('a'):
                            if '/a/friends/add/?' in str(nmx):
                                target.update({'url':nmx['href']})
                        send = ses.get('https://mbasic.facebook.com/'+ target['url'], cookies=__cookies).text
                        if 'Permintaan terkirim' in str(send):
                            print(f' {u}[ {p}{target["name"]}|{target["uid"]}{u} ] {h}Berhasil Mengirim Permintaan {m}{num}')
                            num +=1
                        else:
                            print(f' {u}[ {p}{target["name"]}|{target["uid"]}{u} ] {m}Gagal Mengirim Permintaan ')
                        wait()
            lanjut = page.find('a', string='Lihat selengkapnya')
            if lanjut is None:pass
            else:
                nex.append('https://mbasic.facebook.com/'+ lanjut['href'])

def massAFFWS():
    print(p +'\n Masukan Nama Yang Ingin Dikirim Permintaan Pertemanan.')
    name = input(f'{p} Name: {h}')
    print(f'\n{p} Mass Auto Add From Welcome Search is{h} Running!!!')
    print(o +' ----------------------------------------')
    num = 1
    __cookies = {'cookie':open('user/.cookies', 'r').read()}
    nex = [f'https://mbasic.facebook.com/friends/center/search/?eav=Afbxj3f6R2N5hKDjNhYlhAFaejIV1apne0-uq3xBwkWoJDCJmB93XR261629ebCpMrA&paipv=0&refid=8&search&search_source=welcome_search&q={name}&submit=Cari&mfl_act=2&_rdr#last_acted']
    with r.Session() as ses:
        for url in nex:
            page = bs(ses.get(url, cookies=__cookies).text, 'html.parser')
            for tbody in page.find_all('tbody'):
                if '/friends/hovercard/mbasic/' in str(tbody):
                    if 'Tambah Teman' in str(tbody):
                        target = {}
                        for nm in tbody.find_all('a'):
                            if '/friends/hovercard/mbasic/' in str(nm):
                                target.update({'name':nm.text, 'uid':nm['href'].split('=')[1].split('&')[0]})
                            elif '/a/friends/add/?' in str(nm):
                                target.update({'url':nm['href']})
                        send = ses.get('https://mbasic.facebook.com/'+ target['url'], cookies=__cookies).text
                        if 'Permintaan terkirim' in str(send):
                            print(f' {u}[ {p}{target["name"]}|{target["uid"]}{u} ] {h}Berhasil Mengirim Permintaan {m}{num}')
                            num +=1
                        else:
                            print(f' {u}[ {p}{target["name"]}|{target["uid"]}{u} ] {m}Gagal Mengirim Permintaan ')
                        wait()
            
            lanjut = page.find('a', string='Lihat selengkapnya')
            if lanjut is None:pass
            else:
                nex.append('https://mbasic.facebook.com/'+ lanjut['href'])

def massUnfriends():
    __cookies = {'cookie':open('user/.cookies', 'r').read().replace('\n', '')}
    __token = open('user/.token', 'r').read()
    print(f'\n{p} Mass Auto Add From Welcome Search is{h} Running!!!')
    print(o +' ----------------------------------------')
    num = 1
    try:
        graph = r.get('https://graph.facebook.com/me/friends/?fields=id,name&limit=5000&access_token='+ __token, cookies=__cookies).json()['data']
        with r.Session() as ses:
            for target in graph:
                page = bs(ses.get('https://mbasic.facebook.com/'+ target['id'], cookies=__cookies).text, 'html.parser')
                url = page.find('a', string='Batalkan pertemanan')
                if url is None:pass
                else:
                    confirm = bs(ses.get('https://mbasic.facebook.com/'+ url['href'], cookies=__cookies).text, 'html.parser')
                    if 'Hapus Teman' in str(confirm):
                        form = confirm.find('form', method='post')
                        payl = {}
                        for require in form('input'):
                            payl[require.get('name')] = require.get('value')
                        post = ses.post('https://mbasic.facebook.com/'+ form['action'], data=payl, cookies=__cookies).text
                        if 'Anda tidak lagi berteman dengan' in post:
                            print(f' {u}[ {p}{target["name"]}|{target["id"]}{u} ] {h}Berhasil Menghapus Teman {m}{num}')
                            num +=1
                        else:
                            print(f' {u}[ {p}{target["name"]}|{target["id"]}{u} ] {m}Gagal Dihapus')   
                    else:
                        print(f' {u}[ {p}{target["name"]}|{target["id"]}{u} ] {m}Gagal Dihapus')
    except Exception as e:print(e)#exit(m +' Maaf Sepertinya Akun Anda Bermasalah')
    
#2

def massJGFSN():
    print(p +'\n Masukan Nama Groups Yang Ingin Dimasukin.')
    name = input(f'{p} Name: {h}')
    print(f'\n{p} Mass Auto Add From Welcome Search is{h} Running!!!')
    print(o +' ----------------------------------------')
    num = 1
    __cookies = {'cookie':open('user/.cookies', 'r').read()}
    link = [f'https://mbasic.facebook.com/friends/center/search/?eav=Afbxj3f6R2N5hKDjNhYlhAFaejIV1apne0-uq3xBwkWoJDCJmB93XR261629ebCpMrA&paipv=0&refid=8&search&search_source=welcome_search&q={name}&submit=Cari&mfl_act=2&_rdr#last_acted']
    with r.Session() as ses:
        for url in nex:
            page = bs(ses.get(url, cookies=__cookies).text, 'html.parser')
            for tbody in page.find_all('tbody'):
                if 'Gabung' in str(tbody):
                    pict = tbody.find('img', alt=True)
                    if pict is None:
                        target.update({'name':'Undefined'})
                    else:
                        target.update({'name':pict['alt'].replace(', profile picture', '')})
                    for join in tbody.find_all('a'):
                        if '/a/group/join/?' in str(join):
                            target.update({'id':join['href'].split('group_id=')[1].split('&')[0], 'url':'https://mbasic.facebook.com/'+ join['href']})
                    post = bs(ses.get(target['url'], cookies=__cookies).text, 'html.parser')
                    if post.find('title').text in target['name']:
                        print(f' {u}[ {p}{target["name"]}|{target["id"]}{u} ] {h}Berhasil Memasuki Groups {m}{num}')
                        num +=1
                    elif 'Jawab pertanyaan dari admin berikut. Jawaban Anda akan membantu mereka meninjau permintaan menjadi anggota dan' in str(post):
                        print(f' {u}[ {p}{target["name"]}|{target["id"]}{u} ] {m}Menunggu Persetujuan Admin')   
                    elif 'Batalkan Permintaan' in str(post):
                        print(f' {u}[ {p}{target["name"]}|{target["id"]}{u} ] {m}Menunggu Persetujuan Admin')
                    else:
                        print(f' {u}[ {p}{target["name"]}|{target["id"]}{u} ] {m}Gagal Bergabung')   
                    wait()
            lanjut = page.find('a', string='Lihat Hasil Selanjutnya')
            if lanjut is None:pass
            else:
                link.append(lanjut['href'])


def massLG():
    __cookies = {'cookie':open('user/.cookies', 'r').read().replace('\n', '')}
    print(f'\n{p} Mass Auto Leave Groups is{h} Running!!!')
    print(o +' ----------------------------------------')
    num = 1
    with  r.Session() as ses:
        while True:
            page = bs(ses.get('https://mbasic.facebook.com/groups/?seemore', cookies=__cookies).text, 'html.parser')
            for tbody in page.find_all('tbody'):
                target = {}
                if 'https://mbasic.facebook.com/groups' in str(tbody):
                    groups_id = tbody.find('a', href=True)['href'].replace('https://mbasic.facebook.com/groups/', '').split('/')[0]
                    groups = bs(ses.get(f'https://mbasic.facebook.com/groups/{groups_id}?view=info', cookies=__cookies).text, 'html.parser')
                    if groups.find('title').text == 'Grup':pass
                    else:
                        target.update({'name':groups.find('title').text, 'id':groups_id})
                        leave_url = groups.find('a', string='Keluar dari Grup')
                        if leave_url is None:
                            print(f' {u}[ {p}{target["name"]}|{target["id"]}{u} ] {m}Gagal Keluar Dari Group')
                        else:
                            confirm = bs(ses.get('https://mbasic.facebook.com/'+ leave_url['href'], cookies=__cookies).text, 'html.parser')
                            form = confirm.find('form', method='post')
                            payl = {}
                            for require in form('input'):
                                payl[require.get('name')] = require.get('value')
                            post = ses.post('https://mbasic.facebook.com/'+ form['action'], data=payl, cookies=__cookies).text
                            if 'Gabung ke Grup' in str(post):
                                print(f' {u}[ {p}{target["name"]}|{target["id"]}{u} ] {h}Berhasil Keluar Dari Group {m}{num}')
                                num +=1
                            else:
                                print(f' {u}[ {p}{target["name"]}|{target["id"]}{u} ] {m}Sepertinya Gagal Keluar Dari Group')
                            wait()

#3

def massSMTOO():
    __cookies = {'cookie':open('user/.cookies', 'r').read().replace('\n', '')}
    print(p +'\n Masukan Pesan Yang Ingin Dikirim.')
    text = input(f'{p} Pesan: {h}')
    print(f'\n{p} Mass Auto Send Message is{h} Running!!!')
    print(o +' ----------------------------------------')
    link = ['https://mbasic.facebook.com/messages/']
    num = 1
    with  r.Session() as ses:
        for url in link:
            page = bs(ses.get(url, cookies=__cookies).text, 'html.parser')
            for read in page.find_all('a'):
                target = {}
                if '/messages/read/?' in str(read):
                    target.update({'name':read.text, 'id':read['href'].split('c.')[1].split('%')[0]})
                    msg = bs(ses.get('https://mbasic.facebook.com/'+ read['href'], cookies=__cookies).text, 'html.parser')
                    form = msg.find('form', method='post')
                    payl = {}
                    for require in form('input'):
                        if require.get('name') in ['like', 'send_photo']:pass
                        else:
                            payl[require.get('name')] = require.get('value')
                    payl.update({'body':text, 'send':'Kirim'})
                    post = bs(ses.post('https://mbasic.facebook.com/'+ form['action'], data=payl, cookies=__cookies).text, 'html.parser')
                    if text in str(post):
                        print(f' {u}[ {p}{target["name"]}|{target["id"]}{u} ] {h}Berhasil Mengirim Pesan {m}{num}')
                        num +=1
                    else:
                        print(f' {u}[ {p}{target["name"]}|{target["id"]}{u} ] {h}Gagal Mengirim Pesan')
                    wait()
            lanjut = page.find('a', string='Lihat Pesan Sebelumnya')
            if lanjut is None:pass
            else:
                link.append('https://mbasic.facebook.com/'+lanjut['href'])

def massSMTIO():
    __cookies = {'cookie':open('user/.cookies', 'r').read().replace('\n', '')}
    print(p +'\n Masukan Pesan Yang Ingin Dikirim.')
    text = input(f'{p} Pesan: {h}')
    print(p +'\n Masukan Gambar, contoh:'+m+' /sdcard/gambar.png, gambar.jpg, ../gambar.jpeg')
    img = input(f'{p} Gambar: {h}')
    print(f'\n{p} Mass Auto Send Message is{h} Running!!!')
    print(o +' ----------------------------------------')
    link = ['https://mbasic.facebook.com/messages/']
    num = 1
    with  r.Session() as ses:
        for url in link:
            page = bs(ses.get(url, cookies=__cookies).text, 'html.parser')
            for read in page.find_all('a'):
                target = {}
                if '/messages/read/?' in str(read):
                    target.update({'name':read.text, 'id':read['href'].split('c.')[1].split('%')[0]})
                    msg = bs(ses.get('https://mbasic.facebook.com/'+ read['href'], cookies=__cookies).text, 'html.parser')
                    form = msg.find('form', method='post')
                    payl = {}
                    for require in form('input'):
                        if require.get('name') == 'like':pass
                        else:
                            payl[require.get('name')] = require.get('value')
                    post = bs(ses.post('https://mbasic.facebook.com/'+ form['action'], data=payl, cookies=__cookies).text, 'html.parser')
                    form = post.find('form')
                    payl = {}
                    for require in form('input'):
                        if require.get('name') in ['fb_dtsg', 'jazoest', 'tids', 'ids']:
                            payl[require.get('name')] = require.get('value')
                    payl.update({'body':text})
                    post = ses.post(form['action'], data=payl, files={'file1':open(img, 'rb')}, cookies=__cookies).text
                    if text in str(post):
                        print(f' {u}[ {p}{target["name"]}|{target["id"]}{u} ] {h}Berhasil Mengirim Pesan {m}{num}')
                        num +=1
                    else:
                        print(f' {u}[ {p}{target["name"]}|{target["id"]}{u} ] {h}Gagal Mengirim Pesan')
                    wait()
            lanjut = page.find('a', string='Lihat Pesan Sebelumnya')
            if lanjut is None:pass
            else:
                link.append('https://mbasic.facebook.com/'+lanjut['href'])

def massSMSOO():
    __cookies = {'cookie':open('user/.cookies', 'r').read().replace('\n', '')}
    print(f'\n{p} Mass Auto Send Like in Message is{h} Running!!!')
    print(o +' ----------------------------------------')
    link = ['https://mbasic.facebook.com/messages/']
    num = 1
    with  r.Session() as ses:
        for url in link:
            page = bs(ses.get(url, cookies=__cookies).text, 'html.parser')
            for read in page.find_all('a'):
                target = {}
                if '/messages/read/?' in str(read):
                    target.update({'name':read.text, 'id':read['href'].split('c.')[1].split('%')[0]})
                    msg = bs(ses.get('https://mbasic.facebook.com/'+ read['href'], cookies=__cookies).text, 'html.parser')
                    form = msg.find('form', method='post')
                    payl = {}
                    for require in form('input'):
                        if require.get('name') in ['send_photo']:pass
                        else:
                            payl[require.get('name')] = require.get('value')
                    payl.update({'body':None, 'send':'Kirim'})
                    post = bs(ses.post('https://mbasic.facebook.com/'+ form['action'], data=payl, cookies=__cookies).text, 'html.parser')
                    if 'Baru saja' in str(post):
                        print(f' {u}[ {p}{target["name"]}|{target["id"]}{u} ] {h}Berhasil Mengirim Pesan {m}{num}')
                        num +=1
                    else:
                        print(f' {u}[ {p}{target["name"]}|{target["id"]}{u} ] {h}Gagal Mengirim Pesan')
                    wait()
            lanjut = page.find('a', string='Lihat Pesan Sebelumnya')
            if lanjut is None:pass
            else:
                link.append('https://mbasic.facebook.com/'+lanjut['href'])

def massDLC():
    __cookies = {'cookie':open('user/.cookies', 'r').read().replace('\n', '')}
    print(f'\n{p} Mass Auto Delete Message is{h} Running!!!')
    print(o +' ----------------------------------------')
    link = ['https://mbasic.facebook.com/messages/']
    num = 1
    with  r.Session() as ses:
        for url in link:
            page = bs(ses.get(url, cookies=__cookies).text, 'html.parser')
            for read in page.find_all('a'):
                target = {}
                if '/messages/read/?' in str(read):
                    target.update({'name':read.text, 'id':read['href'].split('c.')[1].split('%')[0]})
                    msg = bs(ses.get('https://mbasic.facebook.com/'+ read['href'], cookies=__cookies).text, 'html.parser')
                    form = msg.find_all('form', method='post')[1]
                    payl = {}
                    print(form)
                    for require in form('input'):
                        if require.get('name') in ['fb_dtsg', 'jazoest', 'delete']:
                            payl[require.get('name')] = require.get('value')
                    post = bs(ses.post('https://mbasic.facebook.com/'+ form['action'], data=payl, cookies=__cookies).text, 'html.parser')
                    delete_url = post.find('a', string='Hapus')
                    if delete_url is None:
                        print(f' {u}[ {p}{target["name"]}|{target["id"]}{u} ] {h}Gagal Menghapus Pesan')
                    else:
                        post = r.get('https://mbasic.facebook.com/'+ delete_url['href'], cookies=__cookies).text
                        if target['name'] in str(post):
                            print(f' {u}[ {p}{target["name"]}|{target["id"]}{u} ] {h}Gagal Menghapus Pesan')
                        else:
                            print(f' {u}[ {p}{target["name"]}|{target["id"]}{u} ] {h}Berhasil Menghapus Pesan {m}{num}')
                            num +=1
                    wait()
            lanjut = page.find('a', string='Lihat Pesan Sebelumnya')
            if lanjut is None:pass
            else:
                link.append('https://mbasic.facebook.com/'+lanjut['href'])

def massBLC():
    __cookies = {'cookie':open('user/.cookies', 'r').read().replace('\n', '')}
    print(f'\n{p} Mass Auto Block Message is{h} Running!!!')
    print(o +' ----------------------------------------')
    link = ['https://mbasic.facebook.com/messages/']
    num = 1
    with  r.Session() as ses:
        for url in link:
            page = bs(ses.get(url, cookies=__cookies).text, 'html.parser')
            for read in page.find_all('a'):
                target = {}
                if '/messages/read/?' in str(read):
                    target.update({'name':read.text, 'id':read['href'].split('c.')[1].split('%')[0]})
                    msg = bs(ses.get('https://mbasic.facebook.com/'+ read['href'], cookies=__cookies).text, 'html.parser')
                    form = msg.find_all('form', method='post')[1]
                    payl = {}
                    for require in form('input'):
                        if require.get('name') in ['fb_dtsg', 'jazoest', 'block_messages']:
                            payl[require.get('name')] = require.get('value')
                    post = bs(ses.post('https://mbasic.facebook.com/'+ form['action'], data=payl, cookies=__cookies).text, 'html.parser')
                    for block_url in post.find_all('a'):
                        if 'Blokir Pesan' in str(block_url):
                            post = r.get('https://mbasic.facebook.com/'+ block_url['href'], cookies=__cookies).text
                            if 'Buka Blokir Pesan' in str(post):
                                print(f' {u}[ {p}{target["name"]}|{target["id"]}{u} ] {h}Berhasil Memblokir Pesan {m}{num}')
                                num +=1
                            else:
                                print(f' {u}[ {p}{target["name"]}|{target["id"]}{u} ] {h}Gagal Memblokir Pesan')
                            wait()
            lanjut = page.find('a', string='Lihat Pesan Sebelumnya')
            if lanjut is None:pass
            else:
                link.append('https://mbasic.facebook.com/'+lanjut['href'])

#4

def massDPT():
    __cookies = {'cookie':open('user/.cookies', 'r').read().replace('\n', '')}
    print(f'\n{p} Mass Auto Block Message is{h} Running!!!')
    print(o +' ----------------------------------------')
    link = ['https://mbasic.facebook.com/me']
    num = 1
    with  r.Session() as ses:
        for url in link:
            page = bs(ses.get(url, cookies=__cookies).text, 'html.parser')
            post_url = page.find_all('a', string='Lainnya', href=True)
            if post_url is None:pass
            else:
                for url in post_url:
                    post_manager = bs(ses.get('https://mbasic.facebook.com'+ url['href'], cookies=__cookies).text, 'html.parser')
                    if 'Postingan ini akan dihapus dari Facebook.' in str(post_manager):
                        form = post_manager.find('form')
                        payl = {}
                        for require in form('input'):
                            if require.get('name') in ['fb_dtsg', 'jazoest', 'submit']:
                                payl[require.get('name')] = require.get('value')
                        payl.update({'action_key':'DELETE'})
                        post = ses.post('https://mbasic.facebook.com/'+ form['action'], data=payl, cookies=__cookies).text
                        if 'Buat Halaman' in str(post):
                            print(h +' Berhasil Menghapus Postingan '+ m +str(num))
                            num +=1
                        else:
                            print(m +' Gagal Menghapus Postingan ')
                    else:
                        print(m +' Gagal Menghapus Postingan ')
                    wait()
            lanjut = page.find('a', string='Lihat Berita Lain')
            if lanjut is None:pass
            else:
                link.append('https://mbasic.facebook.com/'+lanjut['href'])



