# # Dockerfile for this Project

# ## Build and run Docker Image
# ```
# $ docker build -t mm -f 18.dockerfile .
# $ docker run -ti --rm mm bash
# ```

# # Define Base Image
FROM ubuntu:22.04

# # Working Directory for all Files
WORKDIR root

# # User
USER root

# # Copy Repository Files to Docker Image
COPY . .

# # Resynchronize the Package Index
RUN apt-get update

# # Unminimize Ubuntu
RUN yes | unminimize

# # Install and configure Software

# ## Bash Shell

# ### Install Bash Completion
RUN apt-get install -y bash-completion

#
# ### Setup Configuration File (bashrc)
RUN rm -f .bashrc
RUN ln -s 14.bashrc .bashrc

# ## Python3
#
# ### Install Python-3 Base Package
RUN apt-get install -y python3

# ### Install pip Pyhton-Packet-Manager
RUN apt-get install -y pip

# ### Bit-Math: For KiB,MiB and Friends
RUN pip3 install bitmath

# ## Vim Editor
#
# ### Install vim Base Package
RUN apt-get install -y vim

# ### Setup Configuration File (vimrc)
RUN ln -s 13.vimrc .vimrc
