# State Design Pattern Tutorial
* **State Design Pattern** allows an object to change its behavior when its internal state changes.
* It is a behavioral type design pattern.
* It has **_State Interface_** which represents all behaviors (methods) the context will exhibit.
* The **_Concrete States_** in the state design pattern are the implementations of the State Interface that define behaviors specific to each state.
* It has **_Context Class_** that holds a reference to the current state and expose methods to clients.
* Useful to manage states in the applications and swtich between them.
* Easy to maintian since each state is a different class and state-specific behavior is encapsulated in its respective class.
* New states can beeasily added by writing an extra class for the new state.
* E.g. States in a document, states in a game, or different modes in a GUI.
