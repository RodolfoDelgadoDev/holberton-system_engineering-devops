# kills a procces called killmenow

exec {'killmenow':
  command  => 'pkill -9 killmenow',
  provider => 'shell',
}
