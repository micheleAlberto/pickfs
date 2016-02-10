from pick import pick
from glob import glob
import os.path as p

favs={
}
parent_label='#PARENT FOLDER'
this_folder_label='# THIS FOLDER'

def only_filename(path):
    return p.split(path)[-1]

def only_extension(path):
    ext=p.splitext(path)[-1]
    return ext

def _pick_file(f,text,extensions):
    assert(p.isdir(f))
    pattern=p.join(f,'*')
    possible_paths=glob(pattern)
    if extensions:
        possible_paths=[pp for pp in possible_paths if p.isdir(pp) or only_extension(pp) in extensions]
    options=sorted(map(only_filename,possible_paths))
    optionMap={only_filename(path):path for path in possible_paths}
    #opt={only_filename(i):i for i in possible_paths}
    options=[parent_label]+favs.values()+options
    for k in favs:
        optionMap[favs[k]]=k
    a,b=pick(options,text+'\nPath :'+f )
    if  parent_label in a:
        return _pick_file(p.join(f,'..'),text,extensions)
    a=optionMap[a]
    if p.isdir(a):
        return _pick_file(a,text,extensions)
    else:
        return a

def _pick_folder(f,text):
    assert(p.isdir(f))
    pattern=p.join(f,'*')
    possible_paths=glob(pattern)
    possible_paths=[pp for pp in possible_paths if p.isdir(pp)]
    options=sorted(map(only_filename,possible_paths))
    optionMap={only_filename(path):path for path in possible_paths}
    #opt={only_filename(i):i for i in possible_paths}
    options=[this_folder_label,parent_label]+favs.values()+options
    for k in favs:
        optionMap[favs[k]]=k
    a,b=pick(options,text+'\nPath :'+f )
    if  parent_label in a:
        return _pick_folder(p.join(f,'..'),text)
    elif this_folder_label in a:
        return f
    a=optionMap[a]
    if p.isdir(a):
        return _pick_folder(a,text)
    else:
        return a

def pick_file(text='',path='.',extensions=None):
    _exts=None
    if not extensions is None:
        _exts=['.'+e for e in extensions]
    return _pick_file(path,text,_exts)
    
def pick_folder(text='',path='.'):
    return _pick_folder(path,text)






