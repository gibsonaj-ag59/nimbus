from bootstrap_service.api import btstrp_srvc

@btstrp_srvc.route('/get/<string:folder_name>/<string:script_name>')
def get_file(folder_name, script_name):
    *filename, ext = script_name.split('.')
    return open(f'/app/bootstrap_service/static/{folder_name}/{".".join(filename)}.{ext}', 'r').read()
