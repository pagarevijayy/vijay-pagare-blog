+++
title = "Vim Bindings – Cheatsheet & Notes"
date = "2025-08-28T02:23:09+05:30"
description = "Personal VIM cheat sheet. My notes from learning vim."
slug = "vim-bindings"
tags = ["productivity"]
+++
<img src="https://jasonmurray.org/images/vscodevimbindings.png">

#### Personal vim cheat sheet

> impt: command + count + motion


### **Motions**
{{< callout>}}


-- h,j,k,l

-- w: word start (...W)  
-- e: word end (...E)  
-- b: backwards word (...B)  
-- ge: end of previous word 


-- gg: page top  
-- G: page bottom

-- 0: beginning of the line index  
-- $: end of the line <span style="font-size: 14px" class="text-secondary">(trick: use "A" for the end of line + insert mode.) </span>  
-- _: beginning of the line content  <span style="font-size: 14px" class="text-secondary">(trick: use "I" for the beginning of line + insert mode.)</span>    

--  {: move a block of lines up  
--  }: move to a block of lines down  
--  %: goto other pair of the parenthesis 

-- *: occurrence of the word  
{{< /callout>}}

### **Commands**
{{< callout>}}
- y: yank
- d: delete (...D)
- p: paste
- x: delete letter (...X)
- c: change (...C)
- f: find letter and place cursor on it (...F) + ";" to goto next instance.
- t: find letter and place cursor before it (...T) + ";" to goto next instance.
- r: replace letter

- yy: copy line
- dd: delete line

- u: undo
- Ctrl + r: redo

- i: insert mode - before cursor  
- a: insert mode - after cursor (append)

- o: new line below & insert mode
- O: new line above & insert mode

- I: insert at the beginning of the line
- A: append at the end of the line

- v: visual mode
- V: visual line mode

- z: bring the line view to center
- ~: to toggle between upper and lower case
- .: to execute last command
- \>\>: indent right 
- \<\<: indent left
{{< /callout >}}

{{< callout >}}
Esc - exit mode or reset the command  
\: - command mode  
:39: jump to line number 39  
:w - write file  
:q - quit file  
:q! - quit without saving  
:wq - write and quit  

{{< /callout >}}



{{< callout >}}
macros: combination of commands you wanna store in a letter for later execution (just like "." but on steroids)
- q
{{< /callout >}}


Tips: 
- First master motions and essentials commands only, later expand your expertise to niche commands
- Use relative line numbers in editor
- Disable long press for accent characters  <span style="font-size: 14px" class="text-secondary"> i.e. long-press k should give kkkkkk and not ķ. </span>
- Don't stay inside insert mode for long because bindings won't work (get back to normal mode asap)
- Learn and practice via game (if not via actual projects!) 
- Recommended pre-requisite (optional): learn [touch typing](https://www.typing.com/)!
- If you're really going keyboard native, i'd recommend [vimium](https://chromewebstore.google.com/detail/vimium/dbepggeogbaibhgnhhndojpepiihcmeb) - use browser with vim bindings


PS:
- Games: [vim genius](http://www.vimgenius.com/) | [vim adventure](https://vim-adventures.com/)
- Shoutout to [ben](https://www.youtube.com/watch?v=IiwGbcd8S7I) | [primeagen](https://www.youtube.com/watch?v=X6AR2RMB5tE&t=299s)
