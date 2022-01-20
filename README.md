# backup-img-banner
1. Place the main.py file in every individual banner folder. You can either have it in your project skeleton so its ready to go, or cp it from terminal. Here is an example of how to do so one level deep: 

### For copy the main.py file and paste it in every folder in this directory. 
for d in */ ; do
    cp main.py $d/
done

2. Run the main.py file with $python3 main.py. This will have automatically create a cropped image of the banner, name it backup.jpg, and save it in same directory as the main.py file. For multiple banners you can also run the command in a for loop like so: 

### one level deep 

for d in */ ; do
    cd $d/
    python3 main.py
    cd ../
 done

### two levels deep

for d in */ ; do
    cd $d/
    for i in */ ; do
        cd $i/
        python3 main.py
        cd ../
    done
    cd ../
done
