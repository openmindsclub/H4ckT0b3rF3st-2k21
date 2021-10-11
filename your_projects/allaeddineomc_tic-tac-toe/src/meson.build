pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'tic_tac_toe')
gnome = import('gnome')

gnome.compile_resources('tic-tac-toe',
  'tic_tac_toe.gresource.xml',
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
)

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', join_paths(get_option('prefix'), get_option('localedir')))
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'tic-tac-toe.in',
  output: 'tic-tac-toe',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir')
)

tic_tac_toe_sources = [
  '__init__.py',
  'main.py',
]

install_data(tic_tac_toe_sources, install_dir: moduledir)
