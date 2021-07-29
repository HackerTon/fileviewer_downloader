from genericpath import isdir
import io
import json
import os
from shutil import make_archive
import zipfile

from django.http.response import Http404
from django.shortcuts import HttpResponse, render

DIRECTORY = os.environ["DIRECTORY"]

# if DIRECTORY is not defined
if not DIRECTORY:
    



def index(request):
    context = {"filelist": os.listdir(os.path.join(DIRECTORY))}
    return render(request, "base.html", context)


def view_files(request):
    dirs = os.listdir(os.path.join(DIRECTORY))
    classmethod

    return HttpResponse(json.dumps(dirs))


def search_write(path, zip):
    # list all itmes inside of directory PATH
    for thispath in os.listdir(os.path.join(DIRECTORY, path)):
        fullpath = os.path.join(DIRECTORY, path, thispath)
        # verify is the item is a file
        # if yes, then write to our zip
        # if not, then recursive search
        # and write again
        if os.path.isfile(fullpath):
            cur_path = os.path.join(path, thispath)
            zip.write(cur_path)
        else:
            search_write(os.path.join(path, thispath), zip)


def download(request, path):
    relpath = os.path.join(DIRECTORY, path)

    if not os.path.exists(relpath):
        raise Http404("Path {} does not exist".format(relpath))

    # return with zip
    if os.path.isdir(relpath):
        # get current directiry
        cur_directory = os.getcwd()

        # change working directory to DIRECTORY
        os.chdir(DIRECTORY)

        binary = io.BytesIO()
        with zipfile.ZipFile(binary, "x") as zip:
            search_write(path, zip)

        # change working diretory to previos
        # current directory
        os.chdir(cur_directory)

        # reset the head to START OF FILE
        binary.seek(0)

        response = HttpResponse(
            binary,
            headers={
                "Content-Type": "application/zip",
                "Content-Disposition": f"attachment; filename={path}.zip",
            },
        )

        return response

    # return everything with regard to filetype
    if os.path.isfile(relpath):
        file_details = path.split(".")
        if len(file_details) > 2:
            raise Http404("Invalid filename")

        filename = file_details[0]
        filetype = file_details[-1]

        print(f"{filename} {filetype}")

        with open(relpath, "rb") as file:
            response = HttpResponse(
                file,
                headers={
                    "Content-Type": f"application/{filetype}",
                    "Content-Disposition": f"attachment; filename={filename}.{filetype}",
                },
            )

        return response

    raise Http404("system error")