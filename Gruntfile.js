/*!
 * Grunt file
 */

/*jshint node:true */
module.exports = function ( grunt ) {
	grunt.loadNpmTasks( 'grunt-banana-checker' );

	grunt.initConfig( {
		pkg: grunt.file.readJSON( __dirname + '/package.json' ),
		banana: {
			pywikibot: __dirname + '/pywikibot/',
			thirdparty: __dirname + '/thirdparty/',
			add_text: __dirname + '/add_text/',
			archivebot: __dirname + '/archivebot/',
			basic: __dirname + '/basic/',
			blockpageschecker: __dirname + '/blockpageschecker/',
			capitalize_redirects: __dirname + '/capitalize_redirects/',
			casechecker: __dirname + '/casechecker/',
			catall: __dirname + '/catall/',
			category: __dirname + '/category/',
			category_redirect: __dirname + '/category_redirect/',
			clean_sandbox: __dirname + '/clean_sandbox/',
			commons_link: __dirname + '/commons_link/',
			commons: __dirname + '/commons/',
			cosmetic_changes: __dirname + '/cosmetic_changes/',
			delete: __dirname + '/delete/',
			djvutext: __dirname + '/djvutext/',
			editarticle: __dirname + '/editarticle/',
			featured: __dirname + '/featured/',
			fixing_redirects: __dirname + '/fixing_redirects/',
			interwiki: __dirname + '/interwiki/',
			isbn: __dirname + '/isbn/',
			lonelypages: __dirname + '/lonelypages/',
			makecat: __dirname + '/makecat/',
			misspelling: __dirname + '/misspelling/',
			movepages: __dirname + '/movepages/',
			ndashredir: __dirname + '/ndashredir/',
			noreferences: __dirname + '/noreferences/',
			pagefromfile: __dirname + '/pagefromfile/',
			piper: __dirname + '/piper/',
			protect: __dirname + '/protect/',
			pywikibot: __dirname + '/pywikibot/',
			redirect: __dirname + '/redirect/',
			reflinks: __dirname + '/reflinks/',
			replace: __dirname + '/replace/',
			revertbot: __dirname + '/revertbot/',
			selflink: __dirname + '/selflink/',
			solve_disambiguation: __dirname + '/solve_disambiguation/',
			spamremove: __dirname + '/spamremove/',
			spellcheck: __dirname + '/spellcheck/',
			table2wiki: __dirname + '/table2wiki/',
			template: __dirname + '/template/',
			undelete: __dirname + '/undelete/',
			unprotect: __dirname + '/unprotect/',
			unlink: __dirname + '/unlink/',
			//missing messages: weblinkchecker: __dirname + '/weblinkchecker/',
			welcome: __dirname + '/welcome/'
		}
	} );

	grunt.registerTask( 'lint', ['banana'] );
	grunt.registerTask( 'test', ['lint'] );
	grunt.registerTask( 'default', ['test'] );
};
