from flask import Flask

app = Flask(__name__)


@app.route('/run/<float:ratio>')
def run(ratio):
	from kedro.framework.startup import _add_src_to_path, _get_project_metadata
	from kedro.framework.session import KedroSession
	from pathlib import Path

	project_path = Path.cwd()
	metadata = _get_project_metadata(project_path)
	_add_src_to_path(metadata.source_dir, project_path)
	session = KedroSession.create(metadata.package_name, project_path, extra_params={
		'example_test_data_ratio': ratio
	})
	context = session.load_context()
    
	output = context.run()
	return output


if __name__ == '__main__':
    app.run(host='0.0.0.0')