from result import Error, Ok, Result, exception_to_result


@exception_to_result
def to_int(s: str) -> Result[int]:
    return Ok(int(s))


@exception_to_result
def f(s: str) -> Result[None]:
    r = to_int(s)

    # r : Ok | Error -> mypy err
    # print("num is", r.ok())

    if isinstance(r, Error):
        print(r.err_msg)
        return Error(r.err_msg)

    # -> after isinstance(r, Error) -> r : Ok
    print("num is", r.ok())
    return Ok(None)


@exception_to_result
def main() -> Result[None]:
    f("1")
    f("hoge")
    return Ok(None)


if __name__ == "__main__":
    main()
