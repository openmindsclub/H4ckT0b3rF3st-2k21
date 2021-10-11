package main

import (
	"fmt"
	"strings"
	"time"
)

type Avatar struct {
	nickname  string
	strengths []string
	weakness  []string
}

func (a *Avatar) getAvatar() {
		// fmt.Printf("here goes the %s whose strengths are/is %v but also have a weakness which is %v\n",a.nickname, strings.Join(a.strengths, ", "), strings.Join(a.weakness, ", "))
		fmt.Println("fetching user data from database ...")
		time.Sleep(1 * time.Second)
		fmt.Println("match found!")
		time.Sleep(1 * time.Second)
		fmt.Println("-----------------------------------")
		fmt.Printf("nickname: %s\nstrengths: %v\nweakness: %v\n",a.nickname, strings.Join(a.strengths, ", "), strings.Join(a.weakness, ", "))
		fmt.Println("-----------------------------------")
}



func main(){
	avatar1 := &Avatar{
		nickname: "noornee",
		strengths: []string{"html", "python"},
		weakness: []string{"javascipt"},
	}

	// avatar2 := &Avatar{
	// 	nickname: "AnonymousUser ☠",
	// 	strengths: []string{"python", "golang", "javascript", "linux", "rust", },
	// 	weakness: []string{"none"},		
	// }


	avatar1.getAvatar()
	// avatar2.getAvatar()

}