# Copyright (c) Microsoft Corporation. 
# Licensed under the MIT license.

from tree_sitter import Language, Parser

Language.build_library(
  # Store the library in the `build` directory
  '/Users/brendankondracki/Documents/CodeBLEU/parser/my-languages.so',

  # Include one or more languages
  [
    '/Users/brendankondracki/Documents/CodeBLEU/parser/tree-sitter-go',
    '/Users/brendankondracki/Documents/CodeBLEU/parser/tree-sitter-javascript',
    '/Users/brendankondracki/Documents/CodeBLEU/parser/tree-sitter-python',
    '/Users/brendankondracki/Documents/CodeBLEU/parser/tree-sitter-php',
    '/Users/brendankondracki/Documents/CodeBLEU/parser/tree-sitter-java',
    '/Users/brendankondracki/Documents/CodeBLEU/parser/tree-sitter-ruby',
    '/Users/brendankondracki/Documents/CodeBLEU/parser/tree-sitter-c-sharp',
  ]
)

