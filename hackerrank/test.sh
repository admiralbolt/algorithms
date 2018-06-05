#!/bin/bash

input_case="${1/\.py/}_tests/input$2.txt"
output_case="${1/\.py/}_tests/output$2.txt"
output_content=$(<$output_case)
command_result=`python "$1" < "$input_case"`

if [[ "$output_content" == "$command_result" ]]; then
  echo "Test case passed."
else
  echo "Test case failed. Command output: "
  echo "$command_result"
  echo "Test case: "
  echo "$output_content"
fi
