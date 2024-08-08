# Can you change the self-parameter inside a class to something else (say “harry”). Try changing self to “slf” or “harry” and see the effects.

# ==>>YES we change it.



class Stud():
    name="Shreyas"
    dept="Computer"

    #function with Not use of class variable
    def greet(slf):
        print(f"Hello,I am {slf.name}")

s=Stud()
s.greet()