
# Reminder Notifier

This is a simple and intresting python project. This project will help you to create your own reminder notifier for desktop.
A single code base will work on different operationg system like Linux & Windows.




### Source code :

Get the code here : [ https://github.com/mrGain/Reminder](https://github.com/mrGain/Reminder)



  
## Run Locally

Clone the project

```bash
  git clone https://github.com/mrGain/Reminder
```

Go to the project directory

```bash
  $ cd Reminder
```

Install dependencies

```bash
  $ pip install plyer
```
- If you are done just run it.

  
## Usage/Examples
#### Change title and message :
To change your titel and message just assign "title" and "message" by your titel and message.
```python
nf.notify(
            title="write your title here",
            message="write your message here",
            .........
            ..........
        )
```
#### Change the notification icon :
You can download your custom icon based on your requirement.
And put it inside icon folder ,than specify the full name of your icon file with extention(e.g, .png, .ico etc) in place of "glass-of-water.png".
```python
icon = os.path.join(sys.path[0],"icon/glass-of-water.png")
```
  ##### or

After download of your custom icon you can specify icons full path in "app_icon=/... " . Which is shown below.
```python
nf.notify(
            --------
            ---------
            app_icon = "/home/my_pc/myproject/my_custom_icon.ico",
            -------
        )
```

  
## Demo

![Alt text](relative/path/to/img.jpg?raw=true "Title")

  
## Documentation

- Here in my project I used python's default [times module](https://docs.python.org/3/library/time.html)  for getting repeated notification after certain interval.
- For any modification in your program checkout the documentation here : [https://docs.python.org/3/library/time.html](https://docs.python.org/3/library/time.html)

#### 
- To know more about plyer module [click here](https://plyer.readthedocs.io/en/latest/).