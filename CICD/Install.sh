Please follow below instructions to setup the virtual machines:

  1. Download and install vagrant:

    windows:     https://releases.hashicorp.com/vagrant/2.1.1/vagrant_2.1.1_x86_64.msi
    mac:  https://releases.hashicorp.com/vagrant/2.1.1/vagrant_2.1.1_x86_64.dmg

 2. Download and install virtual box:
      windows:          http://download.virtualbox.org/virtualbox/5.1.6/VirtualBox-5.1.6-110634-Win.exe
      mac or other:  http://download.virtualbox.org/virtualbox/5.1.22/VirtualBox-5.1.22-115126-OSX.dmg


 3. Download this github repo and extract the zip file.

    https://github.com/quickfixtech/vagrant-env-setup.git

4. Download putty and winscp :

     putty ::  http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html
  
    winscp:     https://winscp.net/eng/docs/guide_install

      GITBashshell

5. Restart the machine and press F2 or F10 to go into Bios mode. VT-x/AMD-v virtualization must be enabled in BIOS
6.  open cmd prompt in windows machine and go into the unzipped multivagrant directory:

     #cd  env-setup
      #vagrant up 

 7. Enter ip address through putty:

      username /password :  vagrant/vagrant
  Sudo -i
  


#############################################################

Jenkins set up with out root user:

  1. Download tomcat server tar file and Jenkins war file.

      command to download:  wget http://apache.mirrors.tds.net/tomcat/tomcat-8/v8.5.8/bin/apache-tomcat-8.5.8.tar.gz
                  
                                              wget http://mirrors.jenkins.io/war-stable/latest/jenkins.war
  2. Extract apache tomcat tar file.
 
                 cd ~
                 tar -xf apache-tomcat-8.5.8.tar.gz
                 ln -s apache-tomcat-8.5.8 tomcat
 3. Install JDK8 version.

    — Dowload this file form oracle site:
                       http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html
                        jdk-8u131-linux-x64.tar.gz
    
        — Extract the tar file :

        	  cd ~
        	  tar -xf jdk-8u131-linux-x64.tar.gz
       	  ln -s  jdk-8u131 jdk
         
        —  set the JDK path in .bash_profile
             cd ~
             touch .bash_profile

             vi .bash_profile
          
                 JAVA_HOME=~/jdk
                 export PATH=$PATH:$JAVA_HOME/bin
 
             : save the file.
        
         —  Execute this command to set the env path:
                source .bash_profile 
 
           java -version

4. Copy the Jenkins war file into webapps directory.
       cd ~
      cp jenkins.war  ~/tomcat/webapps
5. Start the tomcat server by using below command:
     cd ~/tomcat/bin
     ./catalina.sh start

6. Open the below url in browser:

     https://hostname:8080/jenkins

7. To stop the tomcat server:
     cd ~/tomcat/bin
     ./catalina.sh stop





#########################

Ubuntu with root user:

     https://wiki.jenkins-ci.org/display/JENKINS/Installing+Jenkins+on+Ubuntu:

   Step 1 — Installing Jenkins
    sudo wget -q -O - https://pkg.jenkins.io/debian/jenkins-ci.org.key | sudo apt-key add -  && \
     sudo echo deb http://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list && \
    sudo apt-get update &&\
    sudo apt-get install jenkins -y

   Step 2 — Starting Jenkins
     sudo service start jenkins
    
   Step3:   open the browser.
      http://hostname:8080

Centos or Redhat with root user:

  https://wiki.jenkins-ci.org/display/JENKINS/Installing+Jenkins+on+Red+Hat+distributions


##################################
Maven installation:
 Through vagrant user:
 
      1. Download idk 8  and upload through winscp:

             gitbashshell:   scp jdk-8u131-linux-x64.tar.gz vagrant@192.168.32.5:/tmp

             http://download.oracle.com/otn-pub/java/jdk/8u131-b11/d54c1d3a095b4ff2b6607d096fa80163/jdk-8u131-linux-x64.tar.gz

       2. extract the file
                     tar -xf jdk-8u131-linux-x64.tar.gz
       3. edit .bash_profile
                     #vi ~/.bash_profile
                       JAVA_HOME=~/jdk
                       export PATH=$PATH:$JAVA_HOME/bin
                #source .bash_profile

         maven:    download the maven distribution:
                    1.    wget http://redrockdigimark.com/apachemirror/maven/maven-3/3.5.0/binaries/apache-maven-3.5.0-bin.tar.gz
                     2. tar -xf apache-maven-3.5.0-bin.tar.gz
                     3. set the pathos the maven:
                                #vi ~/.bash_profile
                       MAVEN_HOME=~/maven
                       export PATH=$PATH:$JAVA_HOME/bin:$MAVEN_HOME/bin

                       source .bash_profile

  Through Root user:

    1.. Install JDK8 version.
          sudo apt-get install software-properties-common && \
         sudo add-apt-repository ppa:webupd8team/java -y && \
         sudo apt-get update && \
         sudo apt-get install openjdk-8-jdk -y


         sudo apt-get install oracle-java8-installer -y && \
         sudo apt-get install oracle-java8-set-default 
         #java -version


      sudo apt-get install openjdk-8-jdk

http://openjdk.java.net/install/index.html



2.  install maven:
        
       sudo apt-add-repository ppa:andrei-pozolotin/maven3 && \
       sudo apt-get update && \
       sudo apt-get install maven


####################################
Code Quality Report:

sonar installation:

 
  1. download and configure sonarqube:

Wget https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-5.6.7.zip

  2. extract the sonarqube
 
       unzip sonarqube-5.6.6.zip
  
  3.   # cd sonarqube/bin
        #sonar.sh start

  4. http://Hostname:9000/

  mvn -f pom.xml clean install sonar:sonar
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
   2. install mysql:

         http://sharadchhetri.com/2014/05/07/install-mysql-server-5-6-ubuntu-14-04-lts-trusty-tahr/

       https://gist.github.com/rasheedamir/11460beef67bc6b58d61

      1. sudo apt-get update
        sudo apt-get install mysql-server-5.6

     2. Create SonarQube database and user.
		Command: mysql -u root -p 
CREATE DATABASE sonar CHARACTER SET utf8 COLLATE utf8_general_ci;
CREATE USER ‘sonar’ IDENTIFIED BY ‘sonar';
GRANT ALL ON sonar.* TO ‘sonar’@’%’ IDENTIFIED BY ‘sonar';
GRANT ALL ON sonar.* TO ‘sonar’@’localhost’ IDENTIFIED BY ‘sonar';
FLUSH PRIVILEGES;

########
uncommented in /etc/mysql/my.cnf and assigned to your computers IP address and not loopback
For mysql version 5.7 and above
uncommented in /etc/mysql/mysql.conf.d/mysqld.cnf and assigned to your computers IP address and not loopback
#Replace xxx with your IP Address 
bind-address        = xxx.xxx.xxx.xxx
Or add a bind-address = 0.0.0.0 if you don't want to specify the IP
#########

/usr/share/doc/mysql-server-5.6/README.Debian

Settings.xml


ubuntu@ip-172-31-12-143:~$ cat .m2/settings.xml 
<settings xmlns="http://maven.apache.org/SETTINGS/1.0.0"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/SETTINGS/1.0.0
                      https://maven.apache.org/xsd/settings-1.0.0.xsd">



<profiles>
    <profile>
	<id>sonar</id>
	<properties>
          <!--sonar.jdbc.url>jdbc:mysql://localhost:3306/sonar</sonar.jdbc.url>
          <sonar.jdbc.driver>com.mysql.jdbc.Driver</sonar.jdbc.driver>
          <sonar.jdbc.username>sonar</sonar.jdbc.username>
          <sonar.jdbc.password>xxxxx</sonar.jdbc.password-->
          <!-- SERVER ON A REMOTE HOST -->
          <sonar.host.url>http://ec2-18-216-134-16.us-east-2.compute.amazonaws.com:9000/</sonar.host.url>		
	</properties>
    </profile>
  </profiles>
  <activeProfiles>
    <activeProfile>sonar</activeProfile>
</activeProfiles>

</settings>



##################

Gitlab 

  ssh communication

1. Installation and configuration gitlab.

    https://about.gitlab.com/downloads/#ubuntu1404

    ssh key configuration  — write oparation

2. configurations

       1. deploy key option for read permission

     if i have 2 gitlab server in jenkins server, how you allow multiple keys in your slave machines. ?
  

 add new file to repo:

   1.   git config --global user.name "Sam Smith"
      git config --global user.email sam@example.com

   2. git add —all

   3. git commit -m “message info”

   4. git push origin master


 ### new file in different directory:

      1. git init

      2. git add —all

     3. git commit -m “ message ”

     4. git remote add origin <url>

     5. git pull <url> master
  
     6. git push origin

    git clone --branch <tag_name> <repo_url>



questions:

1. what is git commit

 2. git log
 
 3.  git pull and  git fetch difference 

 4. git rebase and git pull command difference

 5. Various git branching strategies?

 6. git webhooks?

 7. git architecture and workflow?

 8. what is revision ?

Git:

https://www.siteground.com/tutorials/git/commands.htm

https://about.gitlab.com/downloads/#centos7

https://about.gitlab.com/downloads/#ubuntu1404

https://git-scm.com/book/en/v2

https://github.com/gitlabhq/gitlab-recipes/tree/master/install/centos

http://stackoverflow.com/questions/3230074/git-pushing-specific-commit

commands:  http://rogerdudler.github.io/git-guide/


#####################################
https://www.siteground.com/tutorials/git/commands.htm

sudo yum install -y curl policycoreutils-python openssh-server openssh-clients && \
sudo systemctl enable sshd && \
sudo systemctl start sshd && \
sudo firewall-cmd --permanent --add-service=http && \
sudo systemctl reload firewalld && \
sudo yum install postfix && \
sudo systemctl enable postfix && \
sudo systemctl start postfix && \
curl -sS https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.rpm.sh | sudo bash && \
yum install -y gitlab-ce 

##########################
sudo yum install -y curl policycoreutils-python openssh-server cronie && \
sudo lokkit -s http -s ssh && \
sudo yum install postfix && \
sudo service postfix start && \
sudo chkconfig postfix on && \
curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-ee/script.rpm.sh | sudo bash && \
yum install -y gitlab-ce


########################

Gitlabserver setup:
1.Install and configure the necessary dependencies 
 #sudo yum install curl openssh-server openssh-clients postfix cronie
#sudo service postfix start
#sudo chkconfig postfix on
#sudo lokkit -s http -s ssh

2. Add the GitLab package server and install the package 

 #curl -sS https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.rpm.sh | sudo bash
 #sudo yum install gitlab-ce

3.Configure and start GitLab 

 sudo gitlab-ctl reconfigure

4. Browse to the hostname and login 

   http://gitlabserver.example.com/ 


web hook example:

    https://docs.gitlab.com/ce/user/project/integrations/webhooks.html



#####################################
Foreman puppet console installation:

 hostname -f
    6  hostname -i
    7  cat /etc/hostname
    8  cat /etc/hosts
    9  vim /etc/hostname
   10  hostname -f /etc/hostname 
   11  hostname -F /etc/hostname 
   12  cat /etc/hostname
   13  hostname -f
   14  hostname -d
   15  pwd
   16  hostname -b
   17  pwd
   18  sudo sh -c 'echo "deb http://deb.theforeman.org/ trusty 1.5" > /etc/apt/sources.list.d/foreman.list'
   19  sudo sh -c 'echo "deb http://deb.theforeman.org/ plugins 1.5" >> /etc/apt/sources.list.d/foreman.list'
   20  wget -q http://deb.theforeman.org/pubkey.gpg -O- | sudo apt-key add -
   21  sudo apt-get update 
   22  sudo apt-get install foreman-installer
      23  sudo foreman-installer

   if this execute success and hostname as foreman.example.com  will get this message ::::

 	  Success!
	  * Foreman is running at https://foreman.example.com
    	  Default credentials are 'admin:changeme'
 		 * Foreman Proxy is running at https://foreman.example.com:8443
		  * Puppetmaster is running at port 8140
  		The full log is at /var/log/foreman-installer/foreman-installer.log



######################################
Ansible Installation:

  
 sudo apt-get install software-properties-common  && \
  sudo apt-add-repository ppa:ansible/ansible && \
  sudo apt-get update && \
 sudo apt-get install ansible


Centos7

rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm

sudo yum install ansible -y


###########################################
 
Chef DK:

wget https://packages.chef.io/files/stable/chefdk/1.4.3/ubuntu/14.04/chefdk_1.4.3-1_amd64.deb

dpkg -i chefdk_1.4.3-1_amd64.deb

####################################
Ruby:


$ sudo apt-add-repository ppa:brightbox/ruby-ng
$ sudo apt-get update
$ sudo apt-get install ruby2.2

$ ruby2.2 -v


gem install test-kitchen

cat Gemfile >>

   source 'https://rubygems.org'

group :test do
  gem 'kitchen-ansible'
  gem 'kitchen-docker'
  gem 'test-kitchen'
  gem ‘serverspec’
end



bundle install

gem install kitchen-verifier-serverspec
sudo gem install serverspec

bundle exec kitchen init


##################################
1. Set up the repository
Set up the Docker CE repository on Ubuntu. The lsb_release -cs sub-command prints the name of your Ubuntu version, like xenial or trusty.
sudo apt-get -y install \
  apt-transport-https \
  ca-certificates \
  curl  && \

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -  && \

sudo add-apt-repository \
       "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
       $(lsb_release -cs) \
       stable" && \

sudo apt-get update && \
sudo apt-get -y install docker-ce


Redhat7:

sudo yum install -y yum-utils sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo sudo yum makecache fast
sudo yum -y install docker-ce
sudo systemctl start docker
systemctl status docker
systemctl enable docker
docker run hello-world


2. Get Docker CE
Install the latest version of Docker CE on Ubuntu:
	sudo apt-get -y install docker-ce

3. Test your Docker CE installation
Test your installation:
sudo docker run hello-world

commit:

  docker commit 286596825e4b devopsjuly22017/centos-tree:version1
   docker push devopsjuly22017/centos-tree:version1

#######################################


serverspec:

 http://serverspec.org/


https://www.atlassian.com/git/tutorials/comparing-workflows



Linux subsystem for windows to install linux packages in windows machine.


 
1. should be eveloment mode and enabled linux as a subsystem.
 
 

Docker network commands:

  docker network create --subnet=172.18.0.0/16 mynet123

  docker network rm mynet123

 docker run --net mynet123 --ip 172.18.0.22 -itd centos bash


  ip addr

 --hostname

 --add-host


docker commands list reference:
https://docs.docker.com/engine/reference/commandline/rm/ 


 docker run --net mynet234 --ip 172.18.0.22 -i -t -d centos /bin/bash



#################################################
Nagios server setup:
ubuntu: 
https://blog.serverdensity.com/howto-install-nagios-in-30-minutes-and-jumpstart-your-monitoring/    

https://www.digitalocean.com/community/tutorials/how-to-install-nagios-on-centos-6
https://www.digitalocean.com/community/tutorials/how-to-install-nagios-4-and-monitor-your-servers-on-ubuntu-14-04

 Step 1 - Install Packages on Monitoring Server
rpm -Uvh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-6.rpm
yum -y install nagios nagios-plugins-all nagios-plugins-nrpe nrpe php httpd
chkconfig httpd on && chkconfig nagios on
service httpd start && service nagios start
We should also enable SWAP memory on this droplet, at least 2GB:
dd if=/dev/zero of=/swap bs=1024 count=2097152
mkswap /swap && chown root. /swap && chmod 0600 /swap && swapon /swap
echo /swap swap swap defaults 0 0 >> /etc/fstab
echo vm.swappiness = 0 >> /etc/sysctl.conf && sysctl -p
Step 2 - Set Password Protection
Set Nagios Admin Panel Password:
htpasswd -c /etc/nagios/passwd nagiosadmin


url:   http://IP/nagios




Step 4 - Install NRPE on Clients
rpm -Uvh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-6.rpm
yum -y install nagios nagios-plugins-all nrpe
chkconfig nrpe on



Edit /etc/nagios/nrpe.cfg
log_facility=daemon
pid_file=/var/run/nrpe/nrpe.pid
server_port=5666
nrpe_user=nrpe
nrpe_group=nrpe
allowed_hosts=198.211.117.251
dont_blame_nrpe=1
debug=0
command_timeout=60
connection_timeout=300
include_dir=/etc/nrpe.d/
command[check_users]=/usr/lib64/nagios/plugins/check_users -w 5 -c 10
command[check_load]=/usr/lib64/nagios/plugins/check_load -w 15,10,5 -c 30,25,20
command[check_disk]=/usr/lib64/nagios/plugins/check_disk -w 20% -c 10% -p /dev/vda
command[check_zombie_procs]=/usr/lib64/nagios/plugins/check_procs -w 5 -c 10 -s Z
command[check_total_procs]=/usr/lib64/nagios/plugins/check_procs -w 150 -c 200
command[check_procs]=/usr/lib64/nagios/plugins/check_procs -w $ARG1$ -c $ARG2$ -s $ARG3$






iptables -N NRPE
iptables -I INPUT -s 0/0 -p tcp --dport 5666 -j NRPE
iptables -I NRPE -s 198.211.117.251 -j ACCEPT
iptables -A NRPE -s 0/0 -j DROP
/etc/init.d/iptables save




service nrpe start




Step 5 - Add Server Configurations on Monitoring Server
Back on our Monitoring server, we will have to create config files for each of our client servers:
echo "cfg_dir=/etc/nagios/servers" >> /etc/nagios/nagios.cfg
cd /etc/nagios/servers
touch cloudmail.tk.cfg
touch emailocean.tk.cfg



vi /etc/nagios/servers/cloudmail.tk.cfg


define host {
        use                     linux-server
        host_name               cloudmail.tk
        alias                   cloudmail.tk
        address                 198.211.107.218
        }

define service {
        use                             generic-service
        host_name                       cloudmail.tk
        service_description             PING
        check_command                   check_ping!100.0,20%!500.0,60%
        }

define service {
        use                             generic-service
        host_name                       cloudmail.tk
        service_description             SSH
        check_command                   check_ssh
        notifications_enabled           0
        }

define service {
        use                             generic-service
        host_name                       cloudmail.tk
        service_description             Current Load
        check_command                   check_local_load!5.0,4.0,3.0!10.0,6.0,4.0
        }




chown -R nagios. /etc/nagios
service nagios restart



Step 6 - Monitor Hosts in Nagios

###############################
Ubuntu 14.x nagios:

    2  apt-get update
    3  sudo a2enmod rewrite
    4  sudo a2enmod cgi
    5  sudo addgroup --system nagios
    6  sudo addgroup --system nagioscmd
    7  sudo usermod -G nagioscmd www-data
       sudo apt-get install apache2

    
    9  cd
   
   11  $ curl -L -O https://assets.nagios.com/downloads/nagioscore/releases/nagios-4.1.1.tar.gz

   13  tar xvzf nagios-4.1.1.tar.gz
 
   15  cd nagios-4.1.1
  
   17  ./configure --with-nagios-group=nagios --with-command-group=nagioscmd
   18  make all
   19  sudo make install
   20  sudo make install-commandmode
   21  sudo make install-init
   22  sudo make install-config
   23  sudo a2ensite nagios
   24  sudo update-rc.d nagios defaults
   25  sudo htpasswd -c /usr/local/nagios/etc/htpasswd.users nagiosadmin
   26  sudo service apache2 restart
   2
   32  tar xvzf nagios-plugins-2.1.1.tar.gz
   33  cd nagios-plugins-2.1.1
  
   35  ./configure --with-nagios-user=nagios --with-nagios-group=nagios --with-openssl
   36  make
   37  sudo make install

 
 
  
   78  sudo vi /usr/local/nagios/etc/nagios.cfg
   79  sudo mkdir /usr/local/nagios/etc/servers
   80  sudo vi /usr/local/nagios/etc/objects/contacts.cfg
   81  sudo vi /usr/local/nagios/etc/objects/commands.cfg

   85  /usr/local/nagios/bin/nagios -v /usr/local/nagios/etc/nagios.cfg
  
  104  sudo service nagios restart
#######################################################################
Nagios:

   apt-get update
    4  sudo apt-get install apache2 libapache2-mod-php5 php5 apache2-utils
    5  sudo a2enmod rewrite
    6  sudo a2enmod cgi
    7  sudo addgroup --system nagios
    8  sudo addgroup --system nagioscmd
    9  sudo adduser --home /usr/local/nagios --shell /bin/true --ingroup nagioscmd --system nagios
   10  sudo usermod -G nagioscmd www-data
   11  history
   12  cd
   13  $ curl -L -O https://assets.nagios.com/downloads/nagioscore/releases/nagios-4.1.1.tar.gz
   14  cd nagios-4.1.1
   15  ./configure --with-nagios-group=nagios --with-command-group=nagioscmd
   16  make all
   17  sudo make install
   18  sudo make install-commandmode
   19  sudo make install-init
   20  sudo make install-config
   21  sudo a2ensite nagios
   22  sudo update-rc.d nagios defaults
   23  sudo htpasswd -c /usr/local/nagios/etc/htpasswd.users nagiosadmin
   24  sudo service apache2 restart
   25  cd
   26  cd nagios-plugins-2.1.1
   27  history
   28  make
   29  clear
   30  pwd
   31  cd
   32  make all
   33  sudo make install
   34  sudo make install-xinetd
   35  sudo make install-daemon-config
   36  sudo vi /etc/xinetd.d/nrpe
   37  ifconfig
   38  sudo vi /etc/xinetd.d/nrpe
   39  sudo service xinetd restart
   40  sudo vi /usr/local/nagios/etc/nagios.cfg
   41  sudo mkdir /usr/local/nagios/etc/servers
   42  sudo vi /usr/local/nagios/etc/objects/contacts.cfg
   43  sudo vi /usr/local/nagios/etc/objects/commands.cfg
   44  /usr/local/nagios/bin/nagios -v /usr/local/nagios/etc/nagios.cfg
   45  pwd
   46  sudo vi /usr/local/nagios/etc/objects/commands.cfg
   47  sudo service nagios stop
   48  sudo service nagios restart
   49  ps -ef|grep nagios
   50  cd /etc/nagios/servers/
   51  cd /usr/local/nagios/etc/servers
   52  ls -lrt
   53  vim /etc/nagios/servers/ip-172-31-37-231.us-east-2.compute.internal.cfg
   54  pwd
   55  touch ip-172-31-37-231.us-east-2.compute.internal.cfg
   56  vim ip-172-31-37-231.us-east-2.compute.internal.cfg i
   57  vim ip-172-31-37-231.us-east-2.compute.internal.cfg
   58  cd ..
   59  ls -lrt
   60  pwd
   61  cd servers/
   62  chown -R nagios. /usr/local/nagios/etc/servers
   63  ls -lrt
   64  pwd
   65  service nagios restart

   nrpe:

     apt-get update
   sudo apt-get install nagios-nrpe-server nagios-plugins
   
    vim /etc/nagios/nrpe.cfg

            allowed_hosts=127.0.0.1, 192.168.1.100

     sudo /etc/init.d/nagios-nrpe-server restart
     ifconfig
   7 vim /etc/nagios/nrpe.cfg
  sudo /etc/init.d/nagios-nrpe-server restart
  
  cd /usr/lib/nagios/plugins/
   /usr/lib/nagios/plugins/check_disk -w 20% -c 10% -p /dev/hda1
    /usr/lib/nagios/plugins/check_users -w 5 -c 10


Plungins:

 https://www.digitalocean.com/community/tutorials/how-to-create-nagios-plugins-with-python-on-ubuntu-12-10
https://www.howtoforge.com/tutorial/write-a-custom-nagios-check-plugin/

################################
Mcollective:
 http://www.tothenew.com/blog/setting-up-mcollective-and-puppet-push-from-puppetmaster/

#########################
ELK stack:

1. java installation:
    sudo add-apt-repository -y ppa:webupd8team/java
    sudo apt-get update
   sudo apt-get -y install oracle-java8-installer
2. install es:

   wget -qO - https://packages.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
 echo "deb http://packages.elastic.co/elasticsearch/2.x/debian stable main" | sudo tee -a /etc/apt/sources.list.d/elasticsearch-2.x.list  
  sudo apt-get update
 sudo apt-get -y install elasticsearch
 sudo vi /etc/elasticsearch/elasticsearch.yml
       network.host: localhost
 sudo service elasticsearch restart
 sudo update-rc.d elasticsearch defaults 95 10
3. Install Kibana:
   echo "deb http://packages.elastic.co/kibana/4.4/debian stable main" | sudo tee -a /etc/apt/sources.list.d/kibana-4.4.x.list
   sudo apt-get update
   sudo apt-get -y install kibana
   sudo vi /opt/kibana/config/kibana.yml
         server.host: "localhost"
   sudo update-rc.d kibana defaults 96 9
   sudo service kibana start
4. Install nginx:
   sudo apt-get install nginx apache2-utils
   sudo htpasswd -c /etc/nginx/htpasswd.users kibanaadmin
    kibanaadmin
    sudo vi /etc/nginx/sites-available/default

  •	server {
	•	    listen 80;
	•	
	•	    server_name example.com;
	•	
	•	    auth_basic "Restricted Access";
	•	    auth_basic_user_file /etc/nginx/htpasswd.users;
	•	
	•	    location / {
	•	        proxy_pass http://localhost:5601;
	•	        proxy_http_version 1.1;
	•	        proxy_set_header Upgrade $http_upgrade;
	•	        proxy_set_header Connection 'upgrade';
	•	        proxy_set_header Host $host;
	•	        proxy_cache_bypass $http_upgrade;        
	•	    }
	•	}

    sudo service nginx restart
    browse:  http://elk.quickfix.com/

5. Install logstash:
   echo 'deb http://packages.elastic.co/logstash/2.2/debian stable main' | sudo tee /etc/apt/sources.list.d/logstash-2.2.x.list
   sudo apt-get update
   sudo apt-get install logstash
6. generate the ssl certificates:
   sudo mkdir -p /etc/pki/tls/certs
   sudo mkdir /etc/pki/tls/private
   sudo vi /etc/ssl/openssl.cnf
    [ v3_ca ]
       subjectAltName = IP: ELK_server_private_IP
  cd /etc/pki/tls
  sudo openssl req -config /etc/ssl/openssl.cnf -x509 -days 3650 -batch -nodes -newkey rsa:2048 -keyout private/logstash-forwarder.key -out certs/logstash-forwarder.crt
7. configure logstash:

   sudo vi /etc/logstash/conf.d/02-beats-input.conf

   	•	input {
	•	  beats {
	•	    port => 5044
	•	    ssl => true
	•	    ssl_certificate => "/etc/pki/tls/certs/logstash-forwarder.crt"
	•	    ssl_key => "/etc/pki/tls/private/logstash-forwarder.key"
	•	  }
	•	}

 sudo vi /etc/logstash/conf.d/10-syslog-filter.conf
  	•	filter {
	•	  if [type] == "syslog" {
	•	    grok {
	•	      match => { "message" => "%{SYSLOGTIMESTAMP:syslog_timestamp} %{SYSLOGHOST:syslog_hostname} %{DATA:syslog_program}(?:\[%{POSINT:syslog_pid}\])?: %{GREEDYDATA:syslog_message}" }
	•	      add_field => [ "received_at", "%{@timestamp}" ]
	•	      add_field => [ "received_from", "%{host}" ]
	•	    }
	•	    syslog_pri { }
	•	    date {
	•	      match => [ "syslog_timestamp", "MMM  d HH:mm:ss", "MMM dd HH:mm:ss" ]
	•	    }
	•	  }
	•	}


sudo vi /etc/logstash/conf.d/30-elasticsearch-output.conf
  	•	output {
	•	  elasticsearch {
	•	    hosts => ["localhost:9200"]
	•	    sniffing => true
	•	    manage_template => false
	•	    index => "%{[@metadata][beat]}-%{+YYYY.MM.dd}"
	•	    document_type => "%{[@metadata][type]}"
	•	  }
	•	}


sudo service logstash configtest

sudo service logstash restart
sudo update-rc.d logstash defaults 96 9

8. Load Kiban dashboards:
    cd ~
     curl -L -O https://download.elastic.co/beats/dashboards/beats-dashboards-1.1.0.zip
     sudo apt-get -y install unzip
     unzip beats-dashboards-*.zip
     cd beats-dashboards-*
      ./load.sh
When we start using Kibana, we will select the Filebeat index pattern as our default.

9. Load filbeat index template in es

 cd ~
 curl -O https://gist.githubusercontent.com/thisismitch/3429023e8438cc25b86c/raw/d8c479e2a1adcea8b1fe86570e42abab0f10f364/filebeat-index-template.json
 curl -XPUT 'http://localhost:9200/_template/filebeat?pretty' -d@filebeat-index-template.json

10 . setup filbeat:
    scp /etc/pki/tls/certs/logstash-forwarder.crt user@client_server_private_address:/tmp
    sudo mkdir -p /etc/pki/tls/certs
    sudo cp /tmp/logstash-forwarder.crt /etc/pki/tls/certs/
11. Install Filebeat: 
     echo "deb https://packages.elastic.co/beats/apt stable main" |  sudo tee -a /etc/apt/sources.list.d/beats.list
     wget -qO - https://packages.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
     sudo apt-get update
     sudo apt-get install filebeat
12. Configure Filebeat
    sudo vi /etc/filebeat/filebeat.yml
        paths:
        - /var/log/auth.log
        - /var/log/syslog

     logstash:
    # The Logstash hosts
    hosts: ["ELK_server_private_IP:5044"]

    bulk_max_size: 1024

       tls:
      # List of root certificates for HTTPS server verifications
      certificate_authorities: ["/etc/pki/tls/certs/logstash-forwarder.crt"]
 
     sudo service filebeat restart
     sudo update-rc.d filebeat defaults 95 10






#################################################
docker  ELK:


   1. java image:

        docker build -t java_image .

 
  
       2.  es image:

           docker build -t es_image .

   3. logstash image:
       docker build -t logstash_image
   4. Kibana:
       docker build -t kibana_image

   5. boot es:
        docker run --user esuser --name es -d -v es_image
   6. boot log stash:
        docker run -d --name logstash --link es:es logstash_image

   7. Kibana:
       docker run --name kibana --link es:es -d -p 5601:5601 --link es:es kibana_image




############################
Nagios — ubutnu
   
1.  sudo apt-get install apache2 libapache2-mod-php5 php5 apache2-utils





Install Nagios Plugins



#############################
Puppet master:
   wget https://apt.puppetlabs.com/puppetlabs-release-trusty.deb && \

sudo dpkg -i puppetlabs-release-trusty.deb && \

sudo apt-get update -yq && sudo apt-get upgrade -yq && \

sudo apt-get install -yq puppetmaster
   

################################Kubernetes#####################
Setup pre-requisites:
# apt-get update && apt-get install -y apt-transport-https
# apt install docker.io
# systemctl start docker
# systemctl enable docker

# curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add

# vim /etc/apt/sources.list.d/kubernetes.list           
    deb http://apt.kubernetes.io/ kubernetes-xenial main

# apt-get update
# apt-get install -y kubelet kubeadm kubectl kubernetes-cni

Start the cube master:
kubeadm init --apiserver-advertise-address=172.31.18.61


kubectl apply -f https://docs.projectcalico.org/v3.0/getting-started/kubernetes/installation/hosted/kubeadm/1.7/calico.yaml

 kubectl get pods -o wide --all-namespaces

kubectl create -f https://raw.githubusercontent.com/kubernetes/dashboard/master/src/deploy/recommended/kubernetes-dashboard.yaml

kubectl get pods -o wide --all-namespaces

kubectl proxy --address 0.0.0.0 --accept-hosts '.*'

http://ec2-13-232-92-23.ap-south-1.compute.amazonaws.com:8001/api/v1/namespaces/kube-system/services/https:kubernetes-dashboard:/proxy/



kubectl create serviceaccount dashboard -n default
serviceaccount "dashboard" created

root@ip-172-31-16-11:~# kubectl create clusterrolebinding dashboard-admin -n default \
> --clusterrole=cluster-admin \--serviceaccount=default:dashboard

clusterrolebinding.rbac.authorization.k8s.io "dashboard-admin" created

root@ip-172-31-16-11:~# kubectl get secret $(kubectl get serviceaccount dashboard -o jsonpath="{.secrets[0].name}") -o jsonpath="{.data.token}" | base64 --decode

eyJhbGciOiJSUzI1NiIsImtpZCI6IiJ9.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJkZWZhdWx0Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZWNyZXQubmFtZSI6ImRhc2hib2FyZC10b2tlbi1nOHRmMiIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50Lm5hbWUiOiJkYXNoYm9hcmQiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC51aWQiOiI0MTFiMDM4ZS03MGZlLTExZTgtODA0OS0wMjNjNzQ4ZDVlYTQiLCJzdWIiOiJzeXN0ZW06c2VydmljZWFjY291bnQ6ZGVmYXVsdDpkYXNoYm9hcmQifQ.NkViHWIOHe-GliMoDCNWxGhqExBvxVQnQuWbsi5EJr5FtV9UfQGmeQiU1KZw1Vca9foVz5RSz2ETdeZOj04ei82X2NMYd_RjHasJGj9odC2nlqABe3tKcmbKIH-FdLrJG9Ot29g33ySePVWCKqSlrnkqlVwUY311NZe0BCo-tVAM94jvdAZkcoHE6RoOBFHQ3AMbOj3mECtLS2MXhmhLcZ86oQF1IqMyhpQ0mth9W7_YqnqLR-7Rvv2BGcyBEWsbWSQSAYsW0UBF_sNGj43oUhWsNfA2JXElYuC99xQCUMOuYaLg5YyzeSpR3LTvTmKL7CHSwJFArtOiv3DxtdLDEA
root@ip-172-31-16-11:~# 


If you face the login issue:

 Use this:

 Abc.yml
  apiVersion: rbac.authorization.k8s.io/v1beta1
kind: ClusterRoleBinding
metadata:
  name: kubernetes-dashboard
  labels:
    k8s-app: kubernetes-dashboard
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin
subjects:
- kind: ServiceAccount
  name: kubernetes-dashboard
  namespace: kube-system


Kubctl create -f abc.yml

—————
Your Kubernetes master has initialized successfully!

To start using your cluster, you need to run the following as a regular user:

  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config

You should now deploy a pod network to the cluster.
Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
  https://kubernetes.io/docs/concepts/cluster-administration/addons/

You can now join any number of machines by running the following on each node
as root:

  kubeadm join 172.31.16.11:6443 --token j5tms1.oitux199b8ztv6ga --discovery-token-ca-cert-hash sha256:b2c46c62819f5d4d7496f6c8bdfdbd875af29feb9678dd90d57a15396b04f990








https://github.com/kubernetes/dashboard/wiki/Access-control
https://blog.heptio.com/on-securing-the-kubernetes-dashboard-16b09b1b7aca

##########################