# kills a procces called killmenow

exec {'pkill':
  path     => ['usr/bin', 'bin/pkill'],
  command  => 'pkill -9 killmenow',
  provider => 'shell',
}
