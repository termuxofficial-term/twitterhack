B
    SP�]�  �            	   @   s  yDd dl Z d dlmZ d dl Z d dlmZ d dlZd dlZd dlZW n ek
r`   ed� Y nX dZ	dZ
dZe	efZdd	d
ddddddh	ZdZdZdZdZydd� ZW n ek
r�   ed� Y nX edkr�e �d� ed� ed� ed� ed� e�  dS )�    N)�sleep)�tqdmz Ada module yang belum di installzhttps://www.twitter.com/api?Z03711638ab4n29ah28nn39j18Zkhazulyussery0411ZbujangZkontolZpepekZanjingZsayangZcintaZbacotZlonteZayamz[1;31mz[1;32mz[1;36mz[1;33mc              C   s�   t td t d t d t d t �} ybtd� td� xttd��D ]}td� qHW d	}d
�	t
jtjtj |d��}tdt|� � W n   Y nX d S )Nz
[u   ✓�]zusertarget: z
[1;35mSedang mengcrackz----------------�d   g�������?�   � )�ku2   
[1;32m[[1;31m✓[1;32m][1;34mPassword Found: )�input�aa�bb�cc�dd�printr   �ranger   �join�random�choices�stringZascii_uppercaseZdigits�str)Zusername�x�NZres� r   �
twitter.py�usermain   s    (r   ZGoodbyee�__main__�clearug   [1;36m     ╔╦╗╦ ╦╦╔╦╗╔╦╗╔═╗╦═╗  ╦ ╦╔═╗╔═╗╦╔═uR         ║ ║║║║ ║  ║ ║╣ ╠╦╝  ╠═╣╠═╣║  ╠╩╗uR         ╩ ╚╩╝╩ ╩  ╩ ╚═╝╩╚═  ╩ ╩╩ ╩╚═╝╩ ╩z)[5;37;41m	Twitter hacks BETA version[0m)�osZtimer   r   Ztweepyr   r   �ModuleNotFoundErrorr   ZconnectZapikeyZuserkeyZconectZpasswordr
   r   r   r   r   �KeyboardInterrupt�__name__�systemr   r   r   r   �<module>   s>   

