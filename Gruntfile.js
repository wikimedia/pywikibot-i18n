/*!
 * Grunt file
 * https://gruntjs.com/api/grunt.file
 */

/*jshint node:true */
module.exports = function ( grunt ) {
	grunt.loadNpmTasks( 'grunt-banana-checker' );

	grunt.initConfig( {
		banana: {
			all: ['*/', '!log/', '!node_modules/']
		}
	} );

	grunt.registerTask( 'lint', ['banana'] );
	grunt.registerTask( 'test', ['lint'] );
	grunt.registerTask( 'default', ['test'] );
};

