#!/usr/bin/env ruby
puts ARGV[0].scan(/from:(\W*\w+)......(\W*\w+).........(\W*\w*\W*\w*\W*\w*\W*\w*\W*\W*\w*)/).join(separator = ",")
