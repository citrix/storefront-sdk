Citrix Common Authentication Forms Language

#Background

Citrix has devised a common authentication protocol that is implemented by its next generation services and gateway platforms, referred to here as StoreFront Services and NetScaler Gateway. Citrix is implementing client support for this common authentication protocol in native user-agents, such as Receiver and Worx, for the major device platforms, notably: Windows, Mac, iOS, Android, Linux, and Receiver for Web for browser based user-agents.

An important part of the common authentication protocol is a generic forms language, designed to allow third parties to express a wide range of authentication forms using a set of user interface constructs that are similar to basic HTML forms, see RFC 1867 [http://www.ietf.org/rfc/rfc1867.txt] and 2388 [http://www.ietf.org/rfc/rfc2388.txt] for more details.

Third parties can extend the authentication methods supported by StoreFront Services and NetScaler Gateway by implementing server logic that emits and consumes forms defined in the common forms language, see the Citrix Authentication Software Development Kit [1] for more details.

This document is intended for Citrix partners to understand the current expressivity of the common forms language, with the intent to allow them to customize the existing form definitions and to create new forms.

#Receiver Forms Language Overview

Authentication forms are logical forms expressed in Xml, the schema for which is located at: /Schemas/CommonFormsSchema.xsd.

The client controls the rendered form’s layout with minimal hints from the server. These hints define the font size for different types of display text. Enough semantic information is contained in the form description to allow clients to handle credential types appropriately, and to enable credentials to be saved on client machines if permissible.

##Form Structure

The form is structured such that there is a control block, followed a section for authentication requirements.

###Control Block

The form contains the following control information:

- <StateContext> contains any state information that the server wishes the client to hold and pass back with the response to the form.
- <Result> represents the current state of the overall authentication process through a “soft” enumeration.
- <Status> represents a "soft" enumeration of status codes for the current request.
- <LogMessage>  is an optional, localized, message from the server to be displayed, and/or logged by the client.

The following table describes the known result states:

<table border=1 cellpadding=0 cellspacing=0><tr><td width=177><p>more-info<td width=414><p>More information is required by the server. The form contains authentication requirements that should be collected by the client and returned to the server.<tr><td width=177><p>fail<td width=414><p>The authentication conversation has failed. There may be a &lt;LogMessage> to indicate the issue.<tr><td width=177><p>success<td width=414><p>The authentication conversation succeeded<tr><td width=177><p>cancelled<td width=414><p>The authentication conversation was cancelled directly by the user, or indirectly by the user-agent.<tr><td width=177><p>update-credentials<td width=414><p>The user is required to update a credential, such as a password. The form will contain authentication requirements that should be collected by the client and returned to the server.</table>

The following table describes the known status states:

<table border=1 cellpadding=0 cellspacing=0><tr><td width=177><p>success<td width=414><p>The last form POST was successfully processed.<tr><td width=177><p>error-service-unavailable<td width=414><p>The service is unavailable<tr><td width=177><p>error-internal-failure<td width=414><p>An internal error occurred.<tr><td width=177><p>error-params-not-expected<td width=414><p>One or more of the parameters was unexpected.<tr><td width=177><p>error-logon-point-unknown<td width=414><p>The logon point is unknown.<tr><td width=177><p>error-sessionid-invalid<td width=414><p>The associated Http Session state is invalid.<tr><td width=177><p>error-sessionid-expired<td width=414><p>The associated Http Session state has expired.<tr><td width=177><p>error-state-context-invalid<td width=414><p>The session context value was invalid.</table>

***Authentication Requirements***

The first part of the authentication requirements contains information regarding where to send the form response:

- The Url to post the form response to
- The Url to post a cancel request to
- The optional text for the cancel button

The details of how to process the form and construct a form response, can be found in the document: Citrix Common Forms API [2].

The authentication requirements are expressed as an ordered collection of <Requirement> elements, which should generally be arranged in vertical order by the client when displayed. Each requirement element can define: a named credential value, an associated input field, a label, and assistive text. Where desired, the credential and input field can be omitted so the label is used for a heading, message or explanatory text. Common user interaction widgets are supported for input fields: single line clear text edit fields, single line obscured text edit fields, checkboxes, radio buttons, combo-boxes, and submit buttons.

***Credential Types***

The credential types supported are a “soft” enumeration, which means that new credential types can be added without breaking the schema. The mechanism for how credential types are negotiated between the client and the server is described in the document: Citrix Common Forms API [2].

The default credential types are described below. Semantic information is implied for some credential types, to allow clients to provide enhanced handling and other functions.

<table border=1 cellpadding=0 cellspacing=0><tr><td width=177><p>none<td width=414><p>Used for read-only and non-textual input controls.<tr><td width=177><p>username<td width=414><p>The user name which may be qualified, e.g. an Active Directory user principal name such as <a href=mailto:user@fully.qualified.domain>user@fully.qualified.domain</a> or  legacy LAN Manager account such as domain\username.<tr><td width=177><p>domain<td width=414><p>Expected to be an Active Directory domain name, examples include: the shorter legacy LAN Manager format, the fully qualified domain name, or an alternate domain name.<tr><td width=177><p>password<td width=414><p>Textual password or passphrase.<tr><td width=177><p>newpassword<td width=414><p>New password in a change password form.<tr><td width=177><p>pin<td width=414><p>Textual password, likely a short numeric PIN.<tr><td width=177><p>textcredential<td width=414><p>Generic text value with no implied semantics.<tr><td width=177><p>savecredentials<td width=414><p>Control flag for clients that support saving credentials locally.<tr><td width=177><p>realm<td width=414><p>Synonym for domain.<tr><td width=177><p>rsa-passcode<td width=414><p>The current RSA passcode.<tr><td width=177><p>rsa-next-passcode<td width=414><p>The next RSA passcode.<tr><td width=177><p>rsa-next-tokencode<td width=414><p>Secondary RSA tokencode, triggered by one or more invalid tokencodes.<tr><td width=177><p>rsa-pin<td width=414><p>The RSA PIN, used during user generated PIN change.</table>

###Label Types

The label types supported are a “soft” enumeration, which means that new label types can be added without breaking the schema. The mechanism for how label types are negotiated between the client and the server is described in the document: Citrix Common Forms API [2].

Labels can be textual or binary. The only built-in support for binary labels is for images [Label type: image]

***Notes regarding Images:***

- Images are intended for authentication purposes, such as captcha images, and are not intended for generic branding
- The image data supplied in the form is to be interpreted as a Data Uri as defined by RFC 2397, [https://www.ietf.org/rfc/rfc2397.txt]

The following describes the built-in text based labels:

<table border=1 cellpadding=0 cellspacing=0><tr><td width=177><p>none<td width=414><p>No label is associated with the requirement<tr><td width=177><p>plain<td width=414><p>Normal font.<tr><td width=177><p>heading<td width=414><p>Heading font, with appropriate vertical spacing.<tr><td width=177><p>information<td width=414><p>Normal font<tr><td width=177><p>warning<td width=414><p>Warning font<tr><td width=177><p>error<td width=414><p>Error font<tr><td width=177><p>confirmation<td width=414><p>Normal font</table>

***Notes regarding text based labels:***

- If a label type is: none, any textual or binary data specified for the associate label shall be ignored.
- Client implementors may use the label type to decorate messages with icons for visual effect.
- A limited set of inline font markup is supported, within text labels, using standard HTML tags such as: `<b>` for bold, `<i>` for italic, and `<u>` for underline. Note: these style tags must be XML encoded or contained within a CDATA section.
- Messages will flow across multiple lines of display if necessary.
- Client implementations may strip trailing ‘:’ if specified by the form author
- If a label corresponds to an error message, then optionally, the label can also contain a list of credential identifier for requirements associated with the error, that the client can use to highlight the requirements for the users attention.

###Error Highlight Example

Consider a change password form with a requirement for the user to re-enter their existing password:

```
<Requirement>
  <Credential>
    <ID>oldPassword</ID>
    <Type>password</Type>
  </Credential>
  <Label>
    <Text>Old password:</Text>
    <Type>plain</Type>
  </Label>
  <Input>
    <Text>
      <Secret>true</Secret>
      <ReadOnly>false</ReadOnly>
      <InitialValue></InitialValue>
      <Constraint>.+</Constraint>
    </Text>
  </Input>
</Requirement>
```

If the user enters an invalid value, then an error label is returned that specifies the oldpassword requirement to be highlighted:

```
<Requirement>
  <Credential>
    <Type>none</Type>
  </Credential>
  <Label>
    <HighlightFields>
      <CredentialID>oldPassword</CredentialID>
    </HighlightFields>
    <Text>Old password incorrect</Text>
    <Type>error</Type>
  </Label>
  <Input />
</Requirement>
```

![](img/authforms1.png)

This is displayed in Receiver for Windows as:

##Requirement Element Idioms

Examples of the common types of Requirement elements are shown below. Element values that are highlighted identify variable names or user-visible labels that are controlled by the author of the authentication form. Element values that are bolded and underscored indicate field enumeration types defined in this document.

###Cancel Button

The assumption is that forms shall normally have a cancel button, positioned in the natural location for each client platform, relative to the other buttons. However, the cancel button will only be shown if the element is present at: /AuthenticateResponse/AuthenticationRequirements/CancelButtonText.

Notes:
- If a form author specifies CancelButtonText, client implementors may still not show a cancel button if it is not appropriate for the device.
- The absence of CancelButtonText doesn’t preclude the user-agent sending a cancellation request.

###Heading

This example is for a change password form. If a heading is not included as the first requirement element in a form, Receiver clients may provide a default heading that is tailored according to the user action that initiated the authentication process.  

```
<Requirement>
  <Credential>
    <Type>none</Type>
  </Credential>
  <Label>
    <Text>Change Password</Text>
    <Type>heading</Type>
  </Label>
  <Input />
</Requirement>
```

###Message

This example is for an expired password message, added to a change password form for explanation. 

```
<Requirement>
  <Credential>
    <Type>none</Type>
  </Credential>
  <Label>
    <Text>Your password has &lt;b&gt;expired&lt;/b&gt; and must be changed</Text>
    <Type>information</Type>
  </Label>
  <Input />
</Requirement>
```

###Clear Text Credential

This example is for a user name credential type, but could be for a domain or generic value.

```
<Requirement>
  <Credential>
    <ID>username</ID>
    <SaveID>ExplicitForms-Username</SaveID>
    <Type>username</Type>
  </Credential>
  <Label>
    <Text>Username:</Text>
    <Type>plain</Type>
  </Label>
  <Input>
    <Text>
      <Secret>false</Secret>
      <ReadOnly>false</ReadOnly>
      <InitialValue></InitialValue>
      <Constraint>.+</Constraint>
    </Text>
  </Input>
</Requirement>
```

Note: Client implementations may ignore the constraints specified by the form author.

###Secret Text Credential

This credential must keep what the user types a secret, like an `<input>` field of type password in Html.

```
<Requirement>
  <Credential>
    <ID>password</ID>
    <SaveID>ExplicitForms-Password</SaveID>
    <Type>password</Type>
  </Credential>
  <Label>
    <Text>Password:</Text>
    <Type>plain</Type>
  </Label>
  <Input>
    <Text>
      <Secret>true</Secret>
      <ReadOnly>false</ReadOnly>
      <InitialValue></InitialValue>
      <Constraint>.+</Constraint>
    </Text>
  </Input>
</Requirement>
```

###Checkbox

This is one of several input types that typically uses the credential type: none.

```
<Requirement>
  <Credential>
    <ID>userConsent</ID>
    <Type>none</Type>
  </Credential>
  <Label>
    <Text>Accept terms and conditions</Text>
    <Type>plain</Type>
  </Label>
  <Input>
    <CheckBox>
      <InitialValue>false</InitialValue>
    </CheckBox>
  </Input>
</Requirement>
```

###Radio Button

The following demonstrates a series of radio buttons, for the user to select a single item from a set of choices. The <Display> element is typically localized, whereas the <Value> is fixed and is used for defining the initial selection and the value sent to the server.

```
<Requirement>
  <Credential>
    <ID>changePINmode</ID>
    <Type>textcredential</Type>
  </Credential>
  <Label>
    <Text>PIN generation:</Text>
    <Type>plain</Type>
  </Label>
  <Input>
    <RadioButton>
      <InitialSelection>2</InitialSelection>
      <DisplayValues>
        <DisplayValue>
          <Display>Create your own PIN</Display>
          <Value>1</Value>
        </DisplayValue>
        <DisplayValue>
          <Display>Request PIN from authentication system</Display>
          <Value>2</Value>
        </DisplayValue>
      </DisplayValues>
    </RadioButton>
  </Input>
</Requirement>
```

Note for form authors: The initial selection element is optional, and it is the client implementors choice how not having an initial value should be handled.

###Combo Box

A combo-box is almost identical to Radio Button, in that it is used to select a single item. However the hint to the client is that it should be shown as a list control.

```
<Requirement>
  <Credential>
    <ID>Region</ID>
    <Type>textcredential</Type>
  </Credential>
  <Label>
    <Text>Region:</Text>
    <Type>plain</Type>
  </Label>
  <Input>
    <ComboBox>
      <InitialSelection>unspecified</InitialSelection>
      <DisplayValues>
        <DisplayValue>
          <Display>(Select a region)</Display>
          <Value>unspecified</Value>
        </DisplayValue>
        <DisplayValue>
          <Display>United States</Display>
          <Value>US</Value>
        </DisplayValue>
        <DisplayValue>
          <Display>Europe</Display>
          <Value>EU</Value>
        </DisplayValue>
      </DisplayValues>
    </ComboBox>
  </Input>
</Requirement>
```

Note for form authors: The initial selection element is optional, and it is the client implementors choice how not having an initial value should be handled.

###Multi-Combo box

A multi-combo box is similar to a combo box, except multiple selections can be made.

The following multi-combo box, initially has the second item selected.
```
<Requirement>
  <Credential>
    <ID>multiComboId</ID>
    <Type>textcredential</Type>
  </Credential>
  <Label>
    <Text>Multi-select Combo</Text>
    <Type>plain</Type>
  </Label>
  <Input>
    <MultiComboBox>
      <DisplayValues>
        <DisplayValue>
          <Display>Alice</Display>
          <Value>Value1</Value>
        </DisplayValue>
        <DisplayValue>
          <Display>Bob</Display>
          <Value>Value2</Value>
          <Select>true</Select>
        </DisplayValue>
        <DisplayValue>
          <Display>Eve</Display>
          <Value>Value3</Value>
          <Select>false</Select>
        </DisplayValue>
      </DisplayValues>
    </MultiComboBox>
  </Input>
</Requirement>
```

###Save Credentials Control

Saving credentials has important semantic obligations for the client, therefore a distinguished credential type is defined. This allows the form author to control whether the option is presented, and to specify the appropriate localized description.

```
<Requirement>
  <Credential>
    <ID>saveCredentials</ID>
    <Type>savecredentials</Type>
  </Credential>
  <Label>
    <Text>Remember my password</Text>
    <Type>plain</Type>
  </Label>
  <Input>
    <CheckBox>
      <InitialValue>false</InitialValue>
    </CheckBox>
  </Input>
</Requirement>
```

###Submit Button

Multiple buttons can appear in a form, all of them will invoke form submission.
```
			<Requirement>
				<Credential>
					<ID>loginBtn</ID>
					<Type>none</Type>
				</Credential>
				<Label>
					<Type>none</Type>
				</Label>
				<Input>
					<Button>Log on</Button>
				</Input>
			</Requirement>
```

###Assistive Text

Assistive text is optional text to provide more information about an input element to the user. Assistive text may be shown using a tooltip or similar user interface element, but the mechanism for displaying the assistive text is at the discretion of the client. The following example is for a text input with assistive text describing the format required.
```
<Requirement>
  <Credential>
    <ID>username</ID>
    <SaveID>ExplicitForms-Username</SaveID>
    <Type>username</Type>
  </Credential>
  <Label>
    <Text>Username:</Text>
    <Type>plain</Type>
  </Label>
  <Input>
    <AssistiveText>
      Please supply either domain\user or user@fully.qualified.domain.name
    <AssistiveText>
    <Text>
      <Secret>false</Secret>
      <ReadOnly>false</ReadOnly>
      <InitialValue></InitialValue>
      <Constraint>.+</Constraint>
    </Text>
  </Input>
</Requirement>
```

#Detailed Example Forms

##Username, Password, Domain

The following form defines a user name and password form, with the ability to save credentials on the client, assistive text and a cancel button, that renders in Citrix Receiver for Windows as shown below:

![](img/authforms2.png)

Note that the Secure connection marking is supplied by Receiver independently of the form description.

```
<?xml version="1.0" encoding="UTF-8"?>
<AuthenticateResponse xmlns="http://citrix.com/authentication/response/1">
  <Status>success</Status>
  <Result>more-info</Result>
  <StateContext />
  <AuthenticationRequirements>
    <PostBack>/Citrix/Authentication/ExplicitForms/AuthenticateAttempt</PostBack>
    <CancelPostBack>/Citrix/Authentication/ExplicitForms/CancelAuthenticate</CancelPostBack>
    <CancelButtonText>Cancel</CancelButtonText>
    <Requirements>
      <Requirement>
        <Credential>
          <ID>username</ID>
          <SaveID>ExplicitForms-Username</SaveID>
          <Type>username</Type>
        </Credential>
        <Label>
          <Text>User name:</Text>
          <Type>plain</Type>
        </Label>
        <Input>
          <AssistiveText>Please supply either domain\username or user@fully.qualified.domain</AssistiveText>
          <Text>
            <Secret>false</Secret>
            <ReadOnly>false</ReadOnly>
            <InitialValue></InitialValue>
            <Constraint>.+</Constraint>
          </Text>
        </Input>
      </Requirement>
      <Requirement>
        <Credential>
          <ID>password</ID>
          <SaveID>ExplicitForms-Password</SaveID>
          <Type>password</Type>
        </Credential>
        <Label>
          <Text>Password:</Text>
          <Type>plain</Type>
        </Label>
        <Input>
          <Text>
            <Secret>true</Secret>
            <ReadOnly>false</ReadOnly>
            <InitialValue></InitialValue>
            <Constraint>.+</Constraint>
          </Text>
        </Input>
      </Requirement>
      <Requirement>
        <Credential>
          <ID>saveCredentials</ID>
          <Type>savecredentials</Type>
        </Credential>
        <Label>
          <Text>Remember my password</Text>
          <Type>plain</Type>
        </Label>
        <Input>
          <CheckBox>
            <InitialValue>false</InitialValue>
          </CheckBox>
        </Input>
      </Requirement>
      <Requirement>
       <Credential>
         <ID>loginBtn</ID>
         <Type>none</Type>
       </Credential>
       <Label>
         <Type>none</Type>
       </Label>
       <Input>
         <Button>Log On</Button>
       </Input>
      </Requirement>
    </Requirements>
  </AuthenticationRequirements>
</AuthenticateResponse>
```

###Username, Password with Inline Error Message

In the previous example, if the password supplied by the user was incorrect, then the server will return the following form:

```
<?xml version="1.0" encoding="UTF-8"?>
<AuthenticateResponse xmlns="http://citrix.com/authentication/response/1">
  <Status>success</Status>
  <Result>more-info</Result>
  <StateContext />
  <AuthenticationRequirements>
    <PostBack>/Citrix/Authentication/ExplicitForms/AuthenticateAttempt</PostBack>
    <CancelPostBack>/Citrix/Authentication/ExplicitForms/CancelAuthenticate</CancelPostBack>
    <CancelButtonText>Cancel</CancelButtonText>
    <Requirements>
      <Requirement>
        <Credential>
          <ID>username</ID>
          <SaveID>ExplicitForms-Username</SaveID>
          <Type>username</Type>
        </Credential>
        <Label>
          <Text>User name</Text>
          <Type>plain</Type>
        </Label>
        <Input>
          <AssistiveText>Please supply either domain\username or user@fully.qualified.domain</AssistiveText>
          <Text>
            <Secret>false</Secret>
            <ReadOnly>false</ReadOnly>
            <InitialValue>domain\user</InitialValue>
            <Constraint>.+</Constraint>
          </Text>
        </Input>
      </Requirement>
      <Requirement>
        <Credential>
          <ID>password</ID>
          <SaveID>ExplicitForms-Password</SaveID>
          <Type>password</Type>
        </Credential>
        <Label>
          <Text>Password:</Text>
          <Type>plain</Type>
        </Label>
        <Input>
          <Text>
            <Secret>true</Secret>
            <ReadOnly>false</ReadOnly>
            <InitialValue></InitialValue>
            <Constraint>.+</Constraint>
          </Text>
        </Input>
      </Requirement>
      <Requirement>
        <Credential>
          <Type>none</Type>
        </Credential>
        <Label>
          <Text>Incorrect user name or password</Text>
          <Type>error</Type>
        </Label>
        <Input />
      </Requirement>
      <Requirement>
        <Credential>
          <ID>saveCredentials</ID>
          <Type>savecredentials</Type>
        </Credential>
        <Label>
          <Text>Remember my password</Text>
          <Type>plain</Type>
        </Label>
        <Input>
          <CheckBox>
            <InitialValue>false</InitialValue>
          </CheckBox>
        </Input>
      </Requirement>
      <Requirement>
        <Credential>
          <ID>loginBtn</ID>
          <Type>none</Type>
        </Credential>
        <Label>
          <Type>none</Type>
        </Label>
        <Input>
          <Button>Log On</Button>
        </Input>
      </Requirement>
    </Requirements>
  </AuthenticationRequirements>
</AuthenticateResponse>
```
This is rendered by Citrix Receiver for Windows as:

![](img/authforms3.png)

##Username, Password, Domain Selection From List

The following form defines a user name and password form with domain selection from a list, with the ability to save credentials on the client, and a Cancel button, that renders as shown below:
 
![](img/authforms4.png)

```
<?xml version="1.0" encoding="UTF-8"?>
<AuthenticateResponse xmlns="http://citrix.com/authentication/response/1">
  <Status>success</Status>
  <Result>more-info</Result>
  <StateContext />
  <AuthenticationRequirements>
    <PostBack>/Citrix/Authentication/ExplicitForms/AuthenticateAttempt</PostBack>
    <CancelPostBack>/Citrix/Authentication/ExplicitForms/CancelAuthenticate</CancelPostBack>
    <CancelButtonText>Cancel</CancelButtonText>
    <Requirements>
    <Requirement>
      <Credential>
        <Type>none</Type>
      </Credential>
      <Label>
        <Text>Please log on</Text>
        <Type>heading</Type>
      </Label>
      <Input />
    </Requirement>
    <Requirement>
      <Credential>
        <ID>username</ID>
        <SaveID>ExplicitForms-Username</SaveID>
        <Type>username</Type>
      </Credential>
      <Label>
        <Text>User name:</Text>
        <Type>plain</Type>
      </Label>
      <Input>
        <Text>
          <Secret>false</Secret>
          <ReadOnly>false</ReadOnly>
          <InitialValue></InitialValue>
          <Constraint>.+</Constraint>
        </Text>
      </Input>
    </Requirement>
    <Requirement>
      <Credential>
        <ID>password</ID>
        <SaveID>ExplicitForms-Password</SaveID>
        <Type>password</Type>
      </Credential>
      <Label>
        <Text>Password:</Text>
        <Type>plain</Type>
      </Label>
        <Input>
          <Text>
            <Secret>true</Secret>
            <ReadOnly>false</ReadOnly>
            <InitialValue></InitialValue>
            <Constraint>.+</Constraint>
          </Text>
        </Input>
      </Requirement>
      <Requirement>
        <Credential>
          <ID>domain</ID>
          <SaveID>ExplicitForms-Domain</SaveID>
          <Type>domain</Type>
        </Credential>
        <Label>
          <Text>Domain:</Text>
          <Type>plain</Type>
        </Label>
        <Input>
          <ComboBox>
            <InitialSelection>domain</InitialSelection>
            <DisplayValues>
              <DisplayValue>
                <Display>domain</Display>
                <Value>domain</Value>
              </DisplayValue>
              <DisplayValue>
                <Display>other</Display>
                <Value>animaniacs</Value>
              </DisplayValue>
            </DisplayValues>
          </ComboBox>
        </Input>
      </Requirement>
      <Requirement>
        <Credential>
          <ID>saveCredentials</ID>
          <Type>savecredentials</Type>
        </Credential>
        <Label>
          <Text>Remember my password</Text>
          <Type>plain</Type>
        </Label>
        <Input>
          <CheckBox>
            <InitialValue>false</InitialValue>
          </CheckBox>
        </Input>
      </Requirement>
      <Requirement>
        <Credential>
          <ID>loginBtn</ID>
          <Type>none</Type>
        </Credential>
        <Label>
          <Type>none</Type>
        </Label>
        <Input>
          <Button>Log On</Button>
        </Input>
      </Requirement>
    </Requirements>
  </AuthenticationRequirements>
</AuthenticateResponse>
```

When the user fills in their user name and password, selects not to save their password on the client, and the Log On button is activated, then following is returned to the server: 

```
POST https://server/Citrix/Authentication/ExplicitForms/AuthenticateAttempt HTTP/1.1
Content-Type: application/x-www-form-urlencoded
Accept: application/vnd.citrix.authenticateresponse-1+xml, 
        application/vnd.citrix.requesttokenresponse+xml
Accept-Language: en
Host: server
Content-Length: 96
Connection: Keep-Alive
Cache-Control: no-cache
Cookie: ASP.NET_SessionId=abcdefg123456

StateContext=&domain=mydomain&loginBtn=Log+On&password=mypswd&saveCredentials=false&username=me
```

##Change Password

This form is carefully distinguished from other generic credential collection forms, by having a distinct <Result> code in the control block. This is needed so that Receivers which support saving credentials can react appropriately. It includes the user name value as a read-only credential input, and submit both password and newpassword credential values. This form also illustrates the ability to have pre-filled and read-only input fields.

![](img/authforms5.png)

```
<?xml version="1.0" encoding="UTF-8"?>
<AuthenticateResponse xmlns="http://citrix.com/authentication/response/1">
  <Status>success</Status>
  <Result>update-credentials</Result>
  <StateContext/>
  <AuthenticationRequirements>
    <PostBack>/Citrix/Authentication/ExplicitForms</PostBack>
    <CancelPostBack>/Citrix/Authentication/ExplicitForms/Cancel</CancelPostBack>
    <CancelButtonText>Cancel</CancelButtonText>
    <Requirements>
      <Requirement>
        <Credential>
          <Type>none</Type>
        </Credential>
        <Label>
          <Text>Change Expired Password</Text>
          <Type>heading</Type>
        </Label>
        <Input />
      </Requirement>
      <Requirement>
        <Credential>
          <Type>username</Type>
        </Credential>
        <Label>
          <Text>User name:</Text>
          <Type>plain</Type>
        </Label>
        <Input>
          <Text>
            <Secret>false</Secret>
            <ReadOnly>true</ReadOnly>
            <InitialValue>animaniacs\expiredpassword</InitialValue>
            <Constraint>.+</Constraint>
          </Text>
        </Input>
      </Requirement>
      <Requirement>
        <Credential>
          <ID>oldPassword</ID>
          <Type>password</Type>
        </Credential>
        <Label>
          <Text>Old password:</Text>
          <Type>plain</Type>
        </Label>
        <Input>
          <Text>
            <Secret>true</Secret>
            <ReadOnly>false</ReadOnly>
            <InitialValue></InitialValue>
            <Constraint>.+</Constraint>
          </Text>
        </Input>
      </Requirement>
      <Requirement>
        <Credential>
          <ID>newPassword</ID>
          <SaveID>ExplicitForms-Password</SaveID>
          <Type>newpassword</Type>
        </Credential>
        <Label>
          <Text>New password:</Text>
          <Type>plain</Type>
        </Label>
        <Input>
          <Text>
            <Secret>true</Secret>
            <ReadOnly>false</ReadOnly>
            <InitialValue></InitialValue>
            <Constraint>.+</Constraint>
          </Text>
        </Input>
      </Requirement>
      <Requirement>
        <Credential>
          <ID>confirmPassword</ID>
          <Type>newpassword</Type>
        </Credential>
        <Label>
          <Text>Confirm password:</Text>
          <Type>plain</Type>
        </Label>
        <Input>
          <Text>
            <Secret>true</Secret>
            <ReadOnly>false</ReadOnly>
            <InitialValue></InitialValue>
            <Constraint>.+</Constraint>
          </Text>
        </Input>
      </Requirement>
      <Requirement>
        <Credential>
          <ID>changePasswordBtn</ID>
          <Type>none</Type>
        </Credential>
        <Label>
          <Type>none</Type>
        </Label>
        <Input>
          <Button>OK</Button>
        </Input>
      </Requirement>
    </Requirements>
  </AuthenticationRequirements>
</AuthenticateResponse>
```

##Confirmation Message

![](img/authforms6.png)

This example illustrates a message display form that is used to provide important user feedback, such as when the users password has been changed in the example above. This form suppresses the Cancel button to indicate to the user that it is only requesting acknowledgement of a noteworthy state change. The user can still cancel the authentication process in other ways, such as pressing Esc key or using the window close control. Citrix Reciever renders the forms as follows:

```
<?xml version="1.0" encoding="UTF-8"?>
<AuthenticateResponse xmlns="http://citrix.com/authentication/response/1">
  <Status>success</Status>
  <Result>more-info</Result>
  <StateContext />
  <AuthenticationRequirements>
    <PostBack>/Citrix/Authentication/ExplicitForms/ChangePasswordConfirm</PostBack>
    <CancelPostBack></CancelPostBack>
    <Requirements>
      <Requirement>
        <Credential>
          <Type>none</Type>
        </Credential>
        <Label>
          <Text>Your password has been changed successfully.</Text>
          <Type>confirmation</Type>
        </Label>
        <Input />
      </Requirement>
      <Requirement>
        <Credential>
          <ID>changePasswordConfirmBtn</ID>
          <Type>none</Type>
        </Credential>
        <Label>
          <Type>none</Type>
        </Label>
        <Input>
          <Button>OK</Button>
        </Input>
      </Requirement>
    </Requirements>
  </AuthenticationRequirements>
</AuthenticateResponse>
```

##Generic Radius Challenge

![](img/authforms7.png)

This example illustrates the flexibility to have long descriptions and long input fields (without a preceding label), and to control line wrapping by using multiple labels.

```
<?xml version="1.0" encoding="UTF-8"?>
<AuthenticateResponse xmlns="http://citrix.com/authentication/response/1">
	<Status>success</Status>
	<Result>more-info</Result>
	<StateContext />
	<AuthenticationRequirements>
		<PostBack>/serviceLocationPath/ExplicitForms/AuthenticateAttempt</PostBack>
		<CancelPostBack>/serviceLocationPath/ExplicitForms/CancelAuthenticate</CancelPostBack>		   <Requirements>
			<Requirement>
				<Credential>
					<Type>none</Type>
				</Credential>
				<Label>
					<Text>Two-Factor Authentication</Text>
					<Type>heading</Type>
				</Label>
				<Input />
			</Requirement>
			<Requirement>
				<Credential>
					<Type>none</Type>
				</Credential>
				<Label>
					<Text>The authentication system requires more information.</Text>
					<Type>plain</Type>
				</Label>
				<Input />
			</Requirement>
			<Requirement>
				<Credential>
					<Type>none</Type>
				</Credential>
				<Label>
					<Text>PIN accepted. Wait for the tokencode to change then enter the new passcode.</Text>
					<Type>plain</Type>
				</Label>
				<Input />
			</Requirement>
			<Requirement>
				<Credential>
					<ID>challengeResponse</ID>
					<Type>textcredential</Type>
				</Credential>
				<Label><Type>none</Type></Label>
				<Input>
					<Text>
						<Secret>true</Secret>
						<ReadOnly>false</ReadOnly>
						<InitialValue></InitialValue>
						<Constraint>.+</Constraint>
					</Text>
				</Input>
			</Requirement>
			<Requirement>
				<Credential>
					<ID>submitResponseBtn</ID>
					<Type>none</Type>
				</Credential>
				<Label>
					<Type>none</Type>
				</Label>
				<Input>
					<Button>Next</Button>
				</Input>
			</Requirement>
		</Requirements>
	</AuthenticationRequirements>
</AuthenticateResponse>
```

##Change Expired PIN

This example illustrates radio buttons.

![](img/authforms8.png)

```
<?xml version="1.0" encoding="UTF-8"?>
<AuthenticateResponse xmlns="http://citrix.com/authentication/response/1">
	<Status>success</Status>
	<Result>more-info</Result>
	<StateContext />
	<AuthenticationRequirements>
		<PostBack>/serviceLocationPath/ExplicitForms/AuthenticateAttempt</PostBack>
		<CancelPostBack>/serviceLocationPath/ExplicitForms/CancelAuthenticate</CancelPostBack>
		<Requirements>
			<Requirement>
				<Credential>
					<Type>none</Type>
				</Credential>
				<Label>
					<Text>Change Expired PIN</Text>
					<Type>heading</Type>
				</Label>
				<Input />
			</Requirement>
			<Requirement>
				<Credential>
					<Type>none</Type>
				</Credential>
				<Label>
					<Text>After changing your PIN, Receiver prompts you log on again.</Text>
					<Type>plain</Type>
				</Label>
				<Input />
			</Requirement>
			<Requirement>
				<Credential>
					<ID>changePINmode</ID>
					<Type>none</Type>
				</Credential>
				<Label><Type>none</Type></Label>
				<Input>
					<RadioButton>
                <InitialSelection>1</InitialSelection>
						<DisplayValues>
						  <DisplayValue>
						    <Display>Create your own PIN</Display>
						    <Value>1</Value>
						  </DisplayValue>
						  <DisplayValue>
						    <Display>Request PIN from authentication system</Display>
						    <Value>2</Value>
						  </DisplayValue>
						</DisplayValues>
					</RadioButton>
				</Input>
			</Requirement>
			<Requirement>
				<Credential>
					<ID>submitResponseBtn</ID>
					<Type>none</Type>
				</Credential>
				<Label>
					<Type>none</Type>
				</Label>
				<Input>
					<Button>Next</Button>
				</Input>
			</Requirement>
		</Requirements>
	</AuthenticationRequirements>
</AuthenticateResponse>
```
