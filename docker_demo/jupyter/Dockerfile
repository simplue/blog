# ref: https://jupyter-docker-stacks.readthedocs.io/en/latest/using/recipes.html
FROM jupyter/base-notebook:latest

# Create a Python 2.x environment using conda including at least the ipython kernel
# and the kernda utility. Add any additional packages you want available for use
# in a Python 2 notebook to the first line here (e.g., pandas, matplotlib, etc.)
# use conda search to get conda package, like `conda search ipython`
RUN conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/free/ \
    && conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/main/ \
    && conda config --set show_channel_urls yes \
    && conda config --show channels \
    && conda create --quiet --yes -p $CONDA_DIR/envs/python2 python=2.7 ipython ipykernel kernda  \
    && conda clean -tipsy

USER root

# Create a global kernelspec in the image and modify it so that it properly activates
# the python2 conda environment.
RUN $CONDA_DIR/envs/python2/bin/python -m ipykernel install \
    && $CONDA_DIR/envs/python2/bin/kernda -o -y /usr/local/share/jupyter/kernels/python2/kernel.json

USER $NB_USER


# all-kernal-list: https://github.com/jupyter/jupyter/wiki/Jupyter-kernels
# https://github.com/n-riesco/ijavascript
# https://github.com/nearbydelta/itypescript
# with node.js typescript python2 python3 env
RUN mkdir -p /home/jovyan/.pip \
    && printf "[global]\ntimeout = 30\nindex-url = https://mirrors.aliyun.com/pypi/simple/\n" > ~/.pip/pip.conf \
    && ln -s $CONDA_DIR/envs/python2/bin/python $CONDA_DIR/bin/python2 \
    && python2 -m pip install requests \
    && python3 -m pip install requests \
    && npm config set registry https://registry.npm.taobao.org \
    && npm install -g ijavascript && ijsinstall \
    && npm install -g itypescript && its --ts-install=local
