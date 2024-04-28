if __name__ == "__main__":
  # Introduction to Python default parameters

  """
  def function_name(param1, param2 = value2, param3 = value3, ...):
  """

  """
  To use default parameters, you need to place parameters with the default values after other parameters.
  Otherwise, you'll get a syntax error.

  For example, you can not do something like this:

  def function_name(param1 = value1, param2, param3):

  This cause a synyax error
  """

  # Python default parameters example

  def greet(name, message = "Hi"):
    return f"{message} {name}"

  print(greet("John", "Hello"))
  print(greet("John"))
