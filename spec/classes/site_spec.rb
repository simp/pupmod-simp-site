require 'spec_helper'

# rubocop:disable RSpec/Output
puts 'This module has no code in it, so there are no real tests!'
puts 'Here is a whale.'
puts <<-EOF
▄██████████████▄▐█▄▄▄▄█▌
██████▌▄▌▄▐▐▌███▌▀▀██▀▀
████▄█▌▄▌▄▐▐▌▀███▄▄█▌
▄▄▄▄▄██████████████
EOF
# rubocop:enable RSpec/Output

describe 'site' do
  context 'on supported operating systems' do
    on_supported_os.each do |_os, _facts|
      context 'default params' do
        it 'has no code to test' do
          skip 'This module intentionally contains no code'
        end
      end
    end
  end
end
