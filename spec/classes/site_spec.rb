require 'spec_helper'

puts 'This module has no code in it, so there are no real tests!'
puts 'Here is a whale.'
puts <<-EOF
▄██████████████▄▐█▄▄▄▄█▌
██████▌▄▌▄▐▐▌███▌▀▀██▀▀
████▄█▌▄▌▄▐▐▌▀███▄▄█▌
▄▄▄▄▄██████████████
EOF

describe 'site' do
  context 'on supported operating systems' do
    on_supported_os.each do |os, facts|
      context 'default params' do
        it { expect(true).to be_truthy }
      end
    end
  end
end
