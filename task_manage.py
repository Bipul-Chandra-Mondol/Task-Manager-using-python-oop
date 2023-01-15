
from datetime import datetime
import uuid

class Task:
    
    all_task=[]

    def update_task(self,task_num,update_name):
        for task in self.all_task:
            if(task['task_num']==task_num and task['task_done']==False):
                task['task']=update_name
                task['updated_time']=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                print('\nTask Updated Successfully\n')
                break

    def complete_task(self,task_num):
        for task in self.all_task:
            if(task['task_num']==task_num and task['task_done']==False):
                task['task_done']=True
                task['completed_time']=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                print("\nTask Completed Successfully\n")
                break

    def show_all_task(self):
        for task in self.all_task:
            print(f"\nID - {task['id']}")
            print(f"Task - {task['task']}")
            print(f"Created time - {task['created_time']}")
            print(f"updated_time - {task['updated_time']}")
            print(f"Completed - {task['task_done']}")
            print(f"Completed time - {task['completed_time']}")
            print()
    
    def show_incomplete_task(self):
        chk=False
        for task in self.all_task:
            if(task['task_done']==False):
                chk=True
                print(f"ID - {task['id']}")
                print(f"Task - {task['task']}")
                print(f"Created time - {task['created_time']}")
                print(f"updated_time - {task['updated_time']}")
                print(f"Completed - {task['task_done']}")
                print(f"Completed time - {task['completed_time']}")
                print()
        if(chk==False):
            print('No incompleted task')

    def show_completed_task(self):
        chk=False
        for task in self.all_task:
            if(task['task_done']==True):
                chk=True
                print(f"\nID - {task['id']}")
                print(f"Task - {task['task']}")
                print(f"Created time - {task['created_time']}")
                print(f"updated_time - {task['updated_time']}")
                print(f"Completed - {task['task_done']}")
                print(f"Completed time - {task['completed_time']}")
                print()
        if(chk==False):
            print("\nNo completed task\n")

    def check(self):
        for task in self.all_task:
            if(task['task_done']==False):
                return True
        return False

    def show_updateable_task(self):
        for task in self.all_task:
            if(task['task_done']==False):
                print(f"Task No - {task['task_num']}")
                print(f"ID - {task['id']}")
                print(f"Task - {task['task']}")
                print(f"Created time - {task['created_time']}")
                print(f"updated_time - {task['updated_time']}")
                print(f"Completed - {task['task_done']}")
                print(f"Completed time - {task['completed_time']}")
                print()


class TaskCreate(Task):
    task_number=1
    def __init__(self,task) -> None:
        self.task=task
        self.created_time=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.updated_time='NA'
        self.completed_time='NA'
        self.task_done=False

        self.task_num=TaskCreate.task_number
        TaskCreate.task_number+=1

        self.id=uuid.uuid1()

        print("\n Task Created Successfully\n")
        Task.all_task.append(vars(self))


task_manage=Task()

# TaskCreate('Wake up from bed')
# TaskCreate('Take Breakfast')
# obj=Task()
# # obj.show_all_task()
# # obj.show_incomplete_task()
# # obj.show_completed_task()
# sleep(1)
# obj.update_task(1,'Pray to vogoban')
# obj.show_all_task()
# sleep(1)
# obj.complete_task(1)
# obj.show_all_task()

if __name__=="__main__":
    while(True):
        print("1.Add New Task  \n2.Show All Task  \n3.Show Incomplete Tasks  \n4.Show Completed Tasks \n5.Update Tasks \n6.Mark A Task Completed")
        option=int(input("Enter Option: "))

        if(option==1):
            task=input("Enter New Task: ")
            TaskCreate(task)

        elif(option==2):
            task_manage.show_all_task()

        elif(option==3):
            task_manage.show_incomplete_task()

        elif(option==4):
            task_manage.show_completed_task()

        elif(option==5):    # for Updated task
            if(task_manage.check()==True):
                print("\nSelect which task to update")
                task_manage.show_updateable_task()
                num=int(input("Enter Task No: "))
                new_task=input("Enter New Task: ")
                task_manage.update_task(num,new_task)
            else:
                print("\nNo task to update")

        elif(option==6):    # for Completed task
            if(task_manage.check()==True):
                print("\nSelect which task to complete\n")
                task_manage.show_updateable_task()
                n=int(input("Enter Task No: "))
                task_manage.complete_task(n)
            else:
                print("\nNo task to Completed\n")
        
# End of the code