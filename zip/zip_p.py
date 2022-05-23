import zipfile,argparse,os,sys
import subprocess,requests,shutil

src_mock_folder_name = "t1"
dest_mock_folder_name = "t2"

def exec_cmd(cmd_str):
    """
    cmd_str = "{} d {}.apk".format(apktool_path, file_name).split(' ')
    :param cmd_str:
    :return:
    """
    print("start==cmd_str={}".format(cmd_str))
    p = subprocess.Popen(cmd_str, stdin=subprocess.PIPE, 
    stdout=sys.stdout, # stdout=sys.stdout可以输出到命令行
                         stderr=sys.stderr, # stderr=sys.stderr 可以输出到命令行
                         shell=True)
    p.wait()
    print("end==cmd_str={}".format(cmd_str))
    return 0;

def start(srcPath,destPath):

    #先删除旧的
    if os.path.exists(destPath) :
        shutil.rmtree(destPath);
    print("srcPath={}".format(os.path.exists(srcPath)))
    zfile=zipfile.ZipFile(srcPath,"r")
    print("destPath={}".format(destPath))
    zfile.extractall(path=destPath)
    print("extractall success")



def upload(filePath):
    url = 'https://iot.onewo.com/jetlinks/file/static'
    delta_path = os.path.join(f['curPath'], 'update_delta.zip')
    files = {'file': open(delta_path, 'rb')}
    resp = requests.post(url=url, files=files)
    print("==send reply{}reply over==".format(resp.text))


def exec_delta(cmd):
    return exec_cmd(cmd);

parser = argparse.ArgumentParser("1")
# parser.add_argument("-s","--src", type=str)
# parser.add_argument("-d","--dest", type=str)
parser.add_argument("-sv","--srcVer", type=str)
parser.add_argument("-dv","--destVer", type=str)
args = parser.parse_args()
# src = args.src
# dest = args.dest
srcVer = args.srcVer
destVer = args.destVer

f = {
    "curPath" : ""
}

if __name__ == '__main__':
    print("start.")

    cur_file_path = os.path.abspath(__file__)
    curPath = os.path.dirname(cur_file_path)
#    curPath = os.getcwd()
    f['curPath'] = curPath

    src = os.path.join(curPath, "out/target/product/rk3568_r/{sv}.zip".format(sv=srcVer));
    dest = os.path.join(curPath, "out/target/product/rk3568_r/{dv}.zip".format(dv=destVer));

    #解压原版本
    start(srcPath=src,destPath=os.path.join(curPath, src_mock_folder_name));
    #解压目标版本
    start(srcPath=dest,destPath=os.path.join(curPath, dest_mock_folder_name));

    str = os.path.join(curPath, "{mock_folder_name}/build/tools/releasetools/ota_from_target_files".format(mock_folder_name=src_mock_folder_name))
    os.chmod(str,777)

    out = exec_delta("python2.7 {py} --path {path} -i {src} {dest} update_delta.zip"
    .format(py=os.path.join(curPath, "{mock_folder_name}/build/tools/releasetools/ota_from_target_files.py".format(mock_folder_name=src_mock_folder_name)),
    path=os.path.join(curPath, "{mock_folder_name}/out/host/linux-x86".format(mock_folder_name=src_mock_folder_name)),
    src=os.path.join(curPath, "{mock_folder_name}/ota_target_files.zip".format(mock_folder_name=src_mock_folder_name)),
    dest=os.path.join(curPath, "{mock_folder_name}/ota_target_files.zip".format(mock_folder_name=dest_mock_folder_name)))
    )

    upload(1);
    print("stdout={}".format(out))
    print("end.")
