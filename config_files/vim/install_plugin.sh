#!/bin/bash

# install pathogen
mkdir -p ~/.vim/autoload ~/.vim/bundle && \
  curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim
echo 'put execute pathogen#infect() into .vimrc file. See .vimrc example.'


# install another plugins
# search more plugins from https://vimawesome.com/
mkdir -pv ~/.vim/bundle
pushd ~/.vim/bundle
git clone https://github.com/gnattishness/cscope_maps
git clone https://github.com/vim-scripts/taglist.vim
git clone https://github.com/ctrlpvim/ctrlp.vim.git
git clone https://github.com/bronson/vim-trailing-whitespace
git clone https://github.com/scrooloose/syntastic
git clone https://github.com/valloric/youcompleteme
# you might do something more to use youcompleteme
popd
