def main():
    ans = input("Greeting: ")
    ans = ans.strip().lower()
    print("$" + value(ans))

def value(ans):
    if "hello" in ans:
        return 0
    elif ans[0] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()







